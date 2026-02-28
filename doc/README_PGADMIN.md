# Como acessar o banco Docker pelo pgAdmin

Se você usa pgAdmin para visualizar o banco de dados do Docker Compose, siga este passo a passo para não confundir com o banco local:

## 1. Descubra a porta exposta

No docker-compose.yml, o serviço db expõe a porta 5433 do host para a 5432 do container:

```
    ports:
      - '5433:5432'
```

## 2. Adicione um novo servidor no pgAdmin

- Clique com o botão direito em "Servers" > "Register" > "Server..."
- Aba "General":
  - Name: docker
- Aba "Connection":
  - Host name/address: localhost
  - Port: 5433
  - Maintenance database: stepbystep
  - Username: postgres
  - Password: 198870
  - Salve a senha se quiser

## 3. Confirme a conexão

- Expanda o servidor "docker" > Databases > stepbystep > Schemas > public > Tables
- Agora você verá as tabelas criadas pela API (card, alembic_version, etc)

## 4. Dicas

servidor "docker" > Databases > stepbystep > Schemas > public > Tables

- Agora você verá as tabelas criadas pela API (card, alembic_version, etc)

## 4. Dicas

- O servidor "local" (porta 5432) é o Postgres do seu sistema, não o do Docker Compose.
- Sempre use o servidor "docker" (porta 5433) para ver o banco usado pela API.
- Se não aparecerem as tabelas, confira se os containers estão rodando:

  ```bash
  docker ps
  ```

- Se mudar a porta no docker-compose.yml, atualize também no pgAdmin.

Pronto! Assim você nunca confunde o banco do Docker com o local.
