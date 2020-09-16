# Test-Driven Development with FastAPI and Docker
Learn how to build, test, and deploy a text summarization microservice with Python, FastAPI, and Docker

![Continuous Integration and Delivery](https://github.com/kmjawadurrahman/fastapi-tdd-docker/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=master)

## Table of contents
- [About](#about)
  - [Tools and technologies](#tools-and-technologies)
  - [Project structure](#project-structure)
- [Installation](#installation)
    - [1. Clone the repository](#1-clone-the-repository)
    - [2. Use Docker and Docker Compose](#2-use-docker-and-docker-compose)
    - [3. Create the database](#3-create-the-database)
- [Usage](#usage)
    - [Docs](#docs)
    - [Access the database via psql](#access-the-database-via-psql)
- [Tests](#tests)
- [Contributing](#contributing)

## About

**fastapi-tdd-docker** is a code-along to the course **[Test-Driven Development with FastAPI and Docker][tddfastapi]** by Michael Herman.

Link to [original repo](https://github.com/testdrivenio/fastapi-tdd-docker).

#### Tools and technologies

- Python
- [FastAPI](https://fastapi.tiangolo.com/)
- Docker & Docker Compose
- Postgres
- Tortoise ORM
- Pytest
- Uvicorn
- Coverage.py
- flake8
- Black
- isort
- HTTPie
- GitHub Actions
- GitHub Packages
- Gunicorn
- Heroku
- Swagger/OpenAPI

#### Project structure

```
├── .github
│   └── workflows
│       └── main.yml
├── .gitignore
├── README.md
├── docker-compose.yml
├── project
│   ├── .coverage
│   ├── .coveragerc
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── Dockerfile.prod
│   ├── app
│   │   ├── __init__.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── crud.py
│   │   │   ├── ping.py
│   │   │   └── summaries.py
│   │   ├── config.py
│   │   ├── db.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── pydantic.py
│   │   │   └── tortoise.py
│   │   └── summarizer.py
│   ├── db
│   │   ├── Dockerfile
│   │   └── create.sql
│   ├── entrypoint.sh
│   ├── htmlcov
│   ├── requirements-dev.txt
│   ├── requirements.txt
│   ├── setup.cfg
│   └── tests
│       ├── __init__.py
│       ├── conftest.py
│       ├── test_ping.py
│       ├── test_summaries.py
│       └── test_summaries_unit.py
└── release.sh
```

## Installation

Prerequisites:
- Python 3.8+
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

#### 1. Clone the repository

```bash
$ git clone https://github.com/kmjawadurrahman/fastapi-tdd-docker.git && cd fastapi-tdd-docker
```

#### 2. Use Docker and Docker Compose

```bash
$ docker-compose up -d --build
```

#### 3. Create the database

```bash
$ docker-compose exec web python app/db.py
```

## Usage

```bash
$ docker-compose up -d
```

#### Docs

Go to [`http://localhost:8002/docs`](http://localhost:8002/docs).

#### Access the database via psql

```bash
$ docker-compose exec web-db psql -U postgres
```

## Tests

```bash
$ docker-compose exec web python -m pytest
```

Unit Tests with Monkey-patching:

```bash
$ docker-compose exec web pytest -k "unit" -n auto
```

[tddfastapi]: https://testdriven.io/courses/tdd-fastapi/
