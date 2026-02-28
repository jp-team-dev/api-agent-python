# Registro de Continuidade - 2026-02-25

## Mudanças recentes
- Adicionados modelos `Module`, `Lesson` e `Card` com relacionamento guiado.
- Novos esquemas Pydantic para criação/leitura/atualização de módulos, aulas e cards.
- CRUD atualizado para suportar listagens com relacionamentos e filtros por `module_id`/`lesson_id`.
- Router `content` substituído por endpoints `/learning` que expõem módulos, aulas e cards (lista, detalhado, CRUD).
- Migração Alembic `0002_add_guided_models` criada para novas tabelas e colunas (`lesson_id`, `sensory_cue`).
- O campo `sensory_focus` dos módulos agora pode receber múltiplos itens, então os payloads podem enviar listas de estímulos sensoriais, como `["visual", "vocal"]`.
- Lessons, modules e cards agora usam `Pydantic v2` com `ConfigDict(from_attributes=True)` para garantir a serilaização correta dos objetos relacionados.
- Criado `Makefile test` que garante um virtualenv isolado (`.venv-test`) e roda `python -m pytest` contra o mesmo banco PostgreSQL da aplicação (arrays exigem Postgres); manter o serviço (`make up` ou `docker compose up -d db`) é pré-requisito.
- Documentado no README o processo de clonar `stepbystep` → `stepbystep_test` via pgAdmin ou CLI (`createdb -T` / `pg_dump | psql`) e destacada a nova variável `DATABASE_URL` apontando para o clone nos testes.

## Próximos passos recomendados
1. Rodar `make migrate` ou `bash scripts/03-run_migrations.sh` para aplicar `0002_add_guided_models`.
2. Validar endpoints por meio de `http://localhost:8000/learning/docs`.
3. Considerar testes automatizados e documentação adicional para os novos recursos.
