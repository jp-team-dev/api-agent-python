# Evolução da API

Esta checklist documenta o que já foi implementado e os próximos passos para evoluir `api-stepbystep-python`.

## Concluído

| Item | Status | Notas |
| --- | --- | --- |
| Suites de testes de `modules`, `lessons` e `cards` | ✅ | `make test` usa `app/test_learning_api.py`, PostgreSQL real e imprime `TEST_DATABASE_URL`. |
| Ajustes Pydantic v2 (`model_dump`, `exclude_unset`) | ✅ | Substituição de `.dict()` e `.dict(exclude_unset=True)` por `model_dump`. |
| Lifespan handler no FastAPI | ✅ | `app/main.py` usa `asynccontextmanager` para chamar `create_db_and_tables`. |
| Documentação de ambientes, PyCharm/Codex e banco de testes | ✅ | README descreve `.venv`, `.venv-test`, PyCharm e `TEST_DATABASE_URL`. |
| Truncagem segura e compartilhamento de banco nos testes | ✅ | `app/test_learning_api.py` sincroniza `DATABASE_URL` com o teste e usa `sqlalchemy.text`. |

## Em progresso / próximos passos

1. **Cobertura completa das rotas existentes**
   - [ ] Adicionar testes para DELETE/PUT e listar com filtros/paginação para modules/lessons/cards.
   - [ ] Validar cenários de erro (`ResourceNotFoundError`, validações de payload).

2. **Infraestrutura e qualidade**
   - [ ] Configurar lint/format (por exemplo `ruff`/`black`) e documentar uso no README.
   - [ ] Criar workflow GitHub Actions que suba o Postgres (porta 5433), rode `make test` e `alembic upgrade head`.

3. **Usuários, autenticação e progresso**
   - [ ] Introduzir modelos `UserProfile`, `SessionProgress`, `CardFeedback`.
   - [ ] Integrar JWT (FastAPI Users/Auth0) e endpoints para registrar progresso (cards completados, tempo, feedback).

4. **Conteúdos multimídia e personalização**
   - [ ] Expandir `Card` para suportar áudio/vídeo/instruções visuais; adicionar campos de recomendação (ex: `support_level`).
   - [ ] Permitir upload/armazenamento de imagens, áudios e vídeos curtos e criar endpoints de “conteúdo recomendado” e “assets sugeridos” para o app Flutter consumir.

5. **Integração com o Flutter**
   - [ ] Documentar contratos paginados e payloads de admin/upload (inclusive exemplos `curl`).
   - [ ] Adicionar webhook para notificações push ou eventos de progresso (opcional).

## Planejamento
- [ ] Planejar os próximos recursos da lista (usuários/progresso, multimídia, integrações) mantendo o padrão Pydantic v2 e atualizando a documentação conforme cada etapa evolui.
- [ ] Consolidar os requisitos de usuário: autenticação, JWT, controle de sessão e armazenamento de progresso/feedback (conforme a aba “Usuários e progresso”).
- [ ] Descrever o fluxo de multimídia (upload de imagens/áudios/vídeos, catálogo recomendado) e como o Flutter deve consumir essas APIs.

## Observações
- Antes de rodar qualquer teste, mantenha `docker compose up -d db` ativo para garantir o Postgres em `localhost:5433`.
- O `Makefile` já cria `.venv-test` e injeta `TEST_DATABASE_URL`; basta executar `make test`.

Marque o item como concluído conforme avançamos e mantenha este documento atualizado antes de cada sprint.
