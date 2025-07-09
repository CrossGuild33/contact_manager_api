# Decisões Técnicas — Contact Manager API

Este documento descreve as principais decisões técnicas adotadas no desenvolvimento do projeto **Contact Manager API**.

---

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Framework principal**: Flask 3.x
- **Extensões Flask**:
  - Flask-RESTful — Para criação de APIs REST
  - Flask-SQLAlchemy — ORM para integração com banco de dados
  - Flask-CORS — Para habilitar requisições cross-origin
  - Flasgger e flask-openapi3 — Para documentação da API no padrão OpenAPI/Swagger
- **Validação de Dados**: Pydantic
- **Banco de Dados**: SQLite (durante o desenvolvimento)
- **ORM**: SQLAlchemy + SQLAlchemy-Utils
- **Requisições HTTP**: Requests
- **Testes manuais**: Nose (incluído no projeto, mas não implementado nesta versão)
- **Containerização**: Docker

---

## Motivações e Justificativas Técnicas

### Flask
Escolhido pela leveza e facilidade de implementação para APIs REST, além da ampla documentação e suporte pela comunidade.

### SQLite
Selecionado por simplicidade e facilidade de configuração local, ideal para prototipação e desenvolvimento inicial.

### Flask-RESTful + Flask-SQLAlchemy
Permite uma integração prática entre as rotas da API e o banco de dados, reduzindo o boilerplate de código.

### Documentação da API
Uso de **Flasgger** e **flask-openapi3** para criar documentação acessível via Swagger UI, facilitando o consumo da API por outros desenvolvedores.

### Docker
Facilitou a padronização do ambiente entre desenvolvimento e produção, eliminando problemas de “funciona na minha máquina”.

---

## Melhorias Técnicas Futuras

- **Banco de Dados**: Substituir o SQLite por **PostgreSQL** para produção, devido à robustez, escalabilidade e recursos avançados que facilitam o crescimento do projeto.
- **Testes Automatizados**: Implementar testes unitários e de integração, utilizando frameworks como **Pytest** e integração com ferramentas como **Coverage**.
- **CI/CD**: Integrar ferramentas de integração e entrega contínua, como **GitHub Actions** ou **GitLab CI**, para:
  - Rodar testes automáticos
  - Verificar qualidade do código
  - A
