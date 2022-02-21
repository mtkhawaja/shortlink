# shortlink

[![tests](https://github.com/mtkhawaja/shortlink/actions/workflows/main.yml/badge.svg)](https://github.com/mtkhawaja/shortlink/actions/workflows/main.yml)
[![Docker Build](https://github.com/mtkhawaja/shortlink/actions/workflows/docker-image.yml/badge.svg)](https://github.com/mtkhawaja/shortlink/actions/workflows/docker-image.yml)
[![codecov](https://codecov.io/gh/mtkhawaja/shortlink/branch/main/graph/badge.svg?token=I6B4QDNOYI)](https://codecov.io/gh/mtkhawaja/shortlink)
[![Supported Python Version](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

- URL Shortener written in python.

## Quick Start

- Swagger [Documentation](https://shortlink-api.herokuapp.com/docs)

### Docker

#### Bash

##### Build Image & Run Container (sh)

```bash
docker build ./ -t shortlink/api -f ./Dockerfile && \
docker run -it --rm -p 80:8080 shortlink/api
```

##### Build Image & Run Tests (sh)

```bash
docker build --target tests ./ -t shortlink/api-tests -f ./Dockerfile && \
docker run  -it --rm shortlink/api-tests
```

##### Run Application with postgres & redis (sh)

```bash
docker-compose build && docker-compose up
```

#### Powershell

##### Build Image & Run Container (pwsh)

```bash
docker build ./ -t shortlink/api -f ./Dockerfile; `
if ($?) {`
  docker run -it --rm -p 80:8080  shortlink/api; `
}
```

##### Build Image & Run Tests (pwsh)

```bash
docker build --target tests ./ -t shortlink/api-tests -f ./Dockerfile; `
if ($?) {`
  docker run -it --rm shortlink/api-tests; `
}
```

##### Run Application with postgres & redis (pwsh)

```bash
docker-compose build; `
if ($?) {`
  docker-compose up; `
}
```

### Environment Variables

#### General

| Name              | Default | Available Options  | Description                                  |
| ----------------- | ------- | ------------------ | -------------------------------------------- |
| `ENVIRONMENT`     | DEV     | DEV, QA, STG, PROD | Application environment.                     |
| `CONVERSION_BASE` | 64      | 2, 8, 16, 32, 64   | What base to use for shortening record keys. |

#### Logging

| Name                 | Default                                                    | Available Options                     | Description                                                                                                                                                                                                                                    |
| -------------------- | ---------------------------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LOG_FILE`           | `/shortlink/logs/shortlink.log`                            | -                                     | Absolute path for log file. e.g. `/var/log/short-link/application.log` or `E:\logs\short-link\application.log`                                                                                                                                 |
| `LOG_LEVEL`          | INFO                                                       | DEBUG, INFO, WARNING, ERROR, CRITICAL | See python [logging levels](https://docs.python.org/3/library/logging.html#logging-levels) for more information.                                                                                                                               |
| `LOG_FORMAT`         | `%(asctime)s - [%(name)s] - [%(levelname)s] - %(message)s` | -                                     | Log msg format. With the default, formatting, a message may look like: `2022-02-13 13:53:13,463 - [src.main] - [INFO] - Application started.`. See [formatters](https://docs.python.org/3/howto/logging.html#formatters) for more information. |
| `FF_CONSOLE_LOGGING` | True                                                       | True, False                           | If set to true, logs will be directed to console (stdout).                                                                                                                                                                                     |

#### Caching

| Name             | Default | Available Options | Description                                                                                                                                                                                                                                                                                                           |
| ---------------- | ------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `REDIS_USER`     | -       | -                 | Redis username. e.g. short-link-redis-client                                                                                                                                                                                                                                                                          |
| `REDIS_PASSWORD` | -       | -                 | Redis password. e.g. ^E05FNf8*NHqfR*xGIR                                                                                                                                                                                                                                                                              |
| `REDIS_HOST`     | -       | -                 | Redis host name. e.g. redis.example.com                                                                                                                                                                                                                                                                               |
| `REDIS_PORT`     | -       | -                 | Redis port. e.g 6379                                                                                                                                                                                                                                                                                                  |
| `REDIS_URL`      | -       | -                 | Redis connection string based on the following template: 'redis://<redis_user>:<self.redis_password>@<redis_host>:<self.redis_port>'. For example: 'redis://short-link-redis-client:^E05FNf8*NHqfR*xGIR@redis.example.com:6379' **Note**: If `REDIS_URL` is set, all other redis configuration options are overridden |
| `FF_CACHING`     | False   | True, False       | Set to `False` to disable all caching operations.                                                                                                                                                                                                                                                                     |

#### Database

| Name                   | Default | Available Options | Description                                                                                                                                                                                                          |
| ---------------------- | ------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DB_URL`               | -       | -                 | Connection url for the database. For example: 'postgresql+psycopg2://short-link:secret@localhost/sl_db'. See [database urls](https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls) for more information |
| `DB_CONNECT_ARGS`      | -       | -                 | Arguments passed directly to the DBAPIs connect() method See [connect_args](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine.params.connect_args) for more information                   |
| `USE_IN_MEMORY_SQLITE` | True    | True, False       | If set to True, all other database settings are ignored and an in memory sqlite database is used.                                                                                                                    |

## License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
