# Passo a passo para rodar o backend StepByStep

## 1. Pré-requisitos

- Docker e Docker Compose instalados
- (Opcional) Python 3 e pip para rodar scripts locais

## 2. Scripts e ordem sugerida

### 01 - Subir containers e aplicar migrations

```bash
bash scripts/01-dev.sh
```

Ou manualmente:

```bash
docker compose down -v
docker compose up -d
# Aguarde a mensagem "database system is ready to accept connections" nos logs do banco:
docker compose logs db
# Só então rode:
docker compose restart backend
# Agora a API estará disponível em http://localhost:8000/docs
```

### 02 - Resetar banco (opcional, só se quiser limpar tudo)

```bash
bash scripts/02-reset_db.sh
```

Ou manualmente:

```bash
docker compose down -v
docker compose up -d
# Aguarde o banco iniciar, depois:
docker compose restart backend
```

## 3. Testar API

- Acesse http://localhost:8000/docs
- Para ver logs:

```bash
docker compose logs backend
```

## 4. Dicas

- O backend sempre acessa o banco pela porta 5432 (serviço db)
- O host pode usar 5433 para evitar conflito com Postgres local
- Use make up, make migrate, make logs para facilitar

## 5. Scripts sugeridos

Renomeie os scripts para:

- scripts/01-dev.sh
- scripts/02-reset_db.sh

Assim fica fácil saber a ordem.

## 6. Fluxo típico

5433 para evitar conflito com Postgres local

- Use make up, make migrate, make logs para facilitar

## 5. Scripts sugeridos

Renomeie os scripts para:

- scripts/01-dev.sh
- scripts/02-reset_db.sh

Assim fica fácil saber a ordem.

## 6. Fluxo típico

1. Rode 01-dev.sh para subir tudo
2. Acesse <http://localhost:8000/docs>
3. Use 02-reset_db.sh se quiser limpar o banco

Pronto para desenvolver!
