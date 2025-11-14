# 🛒 Orders API & Worker System

Sistema distribuído para gerenciamento de pedidos com arquitetura limpa, mensageria assíncrona e envio de e‑mails simulados via SMTP local.

---

## 📦 Visão Geral

Este projeto é composto por:

- **API de pedidos**: permite cadastro de usuários e criação de pedidos.
- **Worker**: consome mensagens de pedidos e atualiza seus status.
- **RabbitMQ**: mensageria para comunicação assíncrona.
- **PostgreSQL**: banco de dados relacional.
- **Papercut SMTP**: servidor SMTP local para simular envio de e‑mails.

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/marvinho-tn/ordem-de-pedidos-python-api.git
cd ordem-de-pedidos-python-api
```

### 2. Suba os serviços com Docker

```bash
docker compose up -d
```

Isso inicia:
- PostgreSQL em `localhost:5432`
- RabbitMQ em `localhost:5672` (UI em `http://localhost:15672`)
- Papercut SMTP em `localhost:2525` (UI em `http://localhost:8888`)

### 3. Rode a API

```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`  
Documentação Swagger: `http://127.0.0.1:8000/docs`

### 4. Rode o Worker

```bash
cd worker
pip install -r requirements.txt
python main.py
```

---

## ⚙️ Variáveis de ambiente

### 📁 `app/.env`

```env
DATABASE_CONNECTION_STRING=postgresql+psycopg2://admin:1234@postgres:5432/orders_db
RABBITMQ_HOST=rabbitmq
RABBITMQ_USER=admin
RABBITMQ_PASSWORD=1234
```

### 📁 `worker/.env`

```env
ORDERS_API_HOST=http://127.0.0.1:8000
SMTP_HOST=localhost
SMTP_PORT=2525
SMTP_EMAIL_FROM=seu-email@mail.com
RABBITMQ_HOST=localhost
RABBITMQ_USER=admin
RABBITMQ_PASSWORD=1234
```

- **Observação**: é preciso criar o arquivo `.env` na raiz do worker e do app

---

## 🛠 Requisitos

- Python 3.11+
- Docker + Docker Compose
- RabbitMQ, PostgreSQL, SMTP (via compose)

---

## 🌐 URLs úteis

| Serviço       | Descrição                         | URL                                      |
|---------------|-----------------------------------|-------------------------------------------|
| 📬 Papercut    | Interface web do servidor SMTP    | [http://localhost:8888](http://localhost:8888) |
| 🧪 Swagger API | Documentação interativa da API    | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) |
| 🐇 RabbitMQ    | Painel de administração da fila   | [http://localhost:15672](http://localhost:15672) |

---

## 📮 Contato

Desenvolvido por [Marvin Thomaz](mailto:marvinthomaz@gmail.com)  
Projeto em evolução contínua 🚀