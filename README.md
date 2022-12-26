# FastAPI and Docker

![Continuous Integration and Delivery](https://github.com/spyker77/fastapi-tdd-docker/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=main)

## Quick Start

Spin up the containers:

```bash
docker compose up -d --build
```

Generate the database schema on first launch:

```bash
docker compose exec web python init_db.py
```

Open in your browser: <http://localhost:8000/docs>
