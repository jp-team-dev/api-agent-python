# Registro guiado: ordem e exemplos

## Ordem recomendada de cadastro

1. Crie o **module** para cada trilha. A API cobra `POST /learning/modules`.
2. Dentro de cada module, cadastre as **lessons** que organizarão os cards. Use `POST /learning/lessons` apontando `module_id`.
3. Para cada lesson validada, insira os **cards** (`POST /learning/cards`) com `lesson_id`. Cards podem carregar `sensory_cue` para orientar o estímulo sensorial.
4. Ao listar (`GET /learning/modules`, `GET /learning/lessons?module_id=…`, `GET /learning/cards?lesson_id=…`) verifique se os relacionamentos refletem o fluxo `module → lesson → card`.
5. Atualizações seguem o mesmo caminho reverso: revise lesson e card pelo ID específico e utilize os campos `order` para controlar o sequenciamento visual.

## Exemplos de payloads sequenciais

### 1. Modules (5 registros planejados)

| id  | title            | sensory_focus          | order | description                                                                                                       |
| --- | ---------------- | ------------------     | ----- | ----------------------------------------------------------------------------------------------------------------- |
| 1   | Calm Welcome     | ['visual']             | 1     | Introdução com ambiente tranquilo, luz suave e avisos em primeira pessoa.                                         |
| 2   | Shapes & Colors  | ['visual']             | 2     | Explora formas simples e cores contrastantes para reconhecimento.                                                 |
| 3   | Daily Routine    | ['narration']          | 3     | Sequência de atividades do dia com ritmo repetitivo.                                                              |
| 4   | Emotion Cards    | ['vocal']              | 4     | Cartões para identificar emoções básicas usando imagens e áudio.                                                  |
| 5   | Movement Break   | ['proprioception']     | 5     | Mini-atividades com instruções de movimento suave e respiração.                                                   |
| 6   | Sound Journey    | ['auditory']           | 6     | Exploração de sons suaves e repetitivos, como instrumentos simples e natureza, para estimular percepção auditiva. |
| 7   | Touch & Texture  | ['tactile']            | 7     | Atividades com simulação de texturas visuais e instruções de toque, incentivando reconhecimento tátil.            |
| 8   | Story Time       | ['narration']          | 8     | Pequenas histórias narradas com imagens ilustrativas, ajudando na compreensão sequencial e atenção.               |
| 9   | Social Scenarios | ['visual', 'vocal']    | 9     | Cartões que simulam interações sociais básicas (cumprimentos, pedidos), com apoio visual e áudio.                 |
| 10  | Relax & Breathe  | ['proprioception']     | 10    | Exercícios guiados de respiração e relaxamento corporal, com instruções simples e animações suaves.               |

```json
{
  "title": "Social Scenarios",
  "description": "Cartões que simulam interações sociais básicas com apoio visual e áudio.",
  "sensory_focus": ["visual", "vocal"],
  "order": 9
}
```

```json
{
  "title": "Calm Welcome",
  "description": "Primeiro módulo introdutório com poucos estímulos.",
  "sensory_focus": "visual",
  "order": 1
}
```

### 2. Lessons (5 registros — cada um vinculado a um module existente)

| id  | module_id | title           | level        | order |
| --- | --------- | --------------- | ------------ | ----- |
| 1   | 1         | Intro to Touch  | beginner     | 1     |
| 2   | 2         | Shapes in Color | beginner     | 1     |
| 3   | 3         | My Morning      | intermediate | 1     |
| 4   | 4         | How Do I Feel?  | intermediate | 1     |
| 5   | 5         | Gentle Stretch  | beginner     | 1     |

| 6 | 1 | Intro to Test | beginner | 1 |

```json
{
  "module_id": 2,
  "title": "Shapes in Color",
  "description": "Apresenta círculos, quadrados e triângulos em tons pastéis.",
  "level": "beginner",
  "order": 1
}
```

### 3. Cards (5 registros — cada card pertence a uma lesson)

| id  | lesson_id | title        | order | sensory_cue  | image_url                           |
| --- | --------- | ------------ | ----- | ------------ | ----------------------------------- |
| 1   | 1         | Touch Calm   | 1     | soft sound   | https://example.com/calm-hand.png   |
| 2   | 2         | Blue Circle  | 1     | low contrast | https://example.com/blue-circle.png |
| 3   | 3         | Brush Teeth  | 1     | routine tone | https://example.com/toothbrush.png  |
| 4   | 4         | Smiling Face | 1     | happy tone   | https://example.com/smile.png       |
| 5   | 5         | Stretch Arms | 1     | breath cue   | https://example.com/stretch.png     |
| 5   | 5         | Stretch Arms | 1     | breath cue   | <https://example.com/stretch.png>   |

```json
{
  "lesson_id": 4,
  "title": "Smiling Face",
  "description": "Mostra rostos sorridentes e pergunta como a criança se sente.",
  "sensory_cue": "happy tone",
  "order": 1
}
```

## Dicas adicionais

- Use o `order` para garantir que o app visualize as trilhas na sequência desejada; valores menores aparecem primeiro.
- Os campos `sensory_focus` (module) e `sensory_cue` (card) ajudam o Flutter a decidir se deve apresentar áudio, vibrar ou manter silêncio.
- Caso precise reordenar ou remover entidades, exclua primeiro os cards, depois as lessons e só então os modules para preservar integridade referencial.

Atualize este documento sempre que novos módulos, níveis ou cartões forem incluídos para manter o fluxo claro.
