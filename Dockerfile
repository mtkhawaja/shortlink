#
# (0) Setup base image & environment variables.
#
# See python environment variables:
#   https://docs.python.org/3.9/using/cmdline.html#environment-variables
# See Poetry environment variables:
#   https://python-poetry.org/docs/configuration/#using-environment-variables
#

FROM python:3.9-slim-buster as python-base
WORKDIR /shortlink
    # Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    # Poetry
    POETRY_VERSION=1.1.12 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    # Paths
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    # Application
    ENVIRONMENT="DEV" \
    LOG_FILE="/shortlink/logs/shortlink.log" \
    LOG_LEVEL="INFO" \
    FF_CONSOLE_LOGGING="True" \
    CONVERSION_BASE="64" \
    USE_IN_MEMORY_SQLITE="True" \
    FF_CACHING="False"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

    # psycopg2
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl libpq-dev python3-dev gcc

#
# (1) Setup build tools, copy dependency list & install dependencies
#

FROM python-base as builder-base
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock* ./pyproject.toml ./
RUN poetry install  --no-dev --no-root


#
# (2) Run Tests.
#

FROM python-base as tests
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock* ./pyproject.toml ./
RUN poetry install
WORKDIR /shortlink
COPY ./src ./src
COPY ./tests ./tests
CMD pytest tests

#
# (3) Copy source code & setup run configuration.
#

FROM python-base as runnable
WORKDIR /shortlink
COPY ./src ./src
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
CMD uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8080}