from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent, ModelRetry
import logfire

load_dotenv()

logfire.configure()
logfire.instrument_pydantic_ai()


class WeatherForecastResult(BaseModel):
    min: int = Field(description='Min temperature')
    max: int = Field(description='Max temperature')
    is_good: bool = Field(description='If the min temperature is greater than 15 degrees')


class WeatherApiResult(BaseModel):
    min: int
    max: int


weather_agent = Agent(
    'openai:gpt-5',
    instructions=('Você é um agente que fornece a previsão do tempo uma cidade.'
                  'Não responda solicitação não relacionadas a previsão do tempo.'
                  'Caso o usuário não forneça a cidade, pergunte a ele.'),
    output_type=WeatherForecastResult,
    output_retries=3,
)


@weather_agent.tool_plain(retries=3)
def get_weather_forecast(city: str) -> WeatherApiResult:
    """Get the weather forecast of a specific city.

    Args:
        city: city name in lowercase
    """
    if city == 'campinas':
        return WeatherApiResult(min=10, max=20)
    elif city == 'são paulo':
        return WeatherApiResult(min=12, max=18)
    else:
        raise ModelRetry('Cidade não encontrada. Passe somente o nome da cidade em letras minúsculas.')


class BuyBitcoin(BaseModel):
    quantity: float


class SellBitcoin(BaseModel):
    quantity: float


class DoNothing(BaseModel):
    reason: str


crypto_agent = Agent(
    'openai:gpt-5',
    instructions=('Você é um agente especializado em crypto moedas. '
                  'Sua responsabilidade é decidir sobre a compra ou venda de bitcoins.'),
    output_type=BuyBitcoin | SellBitcoin | DoNothing
)


@crypto_agent.tool_plain()
def get_current_bitcoin_price() -> float:
    """Get current price of bitcoin
    """
    return 352546.34


@crypto_agent.tool_plain()
def get_bitcoin_news() -> str:
    """Get the recent news about bitcoin
    """
    return 'Alta na bitcoin por conta de xyz'


try:
    result = crypto_agent.run_sync('Me fale o que devo fazer agora com meus bitcoins')
    print(result.output)
except:
    print('Cenário de erro')