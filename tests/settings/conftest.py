import tempfile
import uuid
from datetime import datetime
from typing import Generator
from unittest.mock import Mock

import pytest

from src.db.schemas.short_link_schemas import ShortLinkResponse


@pytest.fixture
def log_level() -> Generator[str, None, None]:
    yield "INFO"


@pytest.fixture
def log_format() -> Generator[str, None, None]:
    yield "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


@pytest.fixture
def log_file() -> Generator[str, None, None]:
    yield tempfile.NamedTemporaryFile(mode="w").name


@pytest.fixture
def redis_user() -> Generator[str, None, None]:
    yield "redis-user"


@pytest.fixture
def redis_password() -> Generator[str, None, None]:
    yield "redis-password"


@pytest.fixture
def redis_port() -> Generator[str, None, None]:
    yield "54789"


@pytest.fixture
def redis_host() -> Generator[str, None, None]:
    yield "test.redis.example.com"


@pytest.fixture
def key_string() -> Generator[str, None, None]:
    yield "112z2z"


@pytest.fixture
def original_url() -> Generator[str, None, None]:
    yield "www.example.com"


@pytest.fixture
def mock_redis_client() -> Generator[Mock, None, None]:
    yield Mock()


@pytest.fixture
def short_link_response(original_url: str, key_string: str) -> Generator[ShortLinkResponse, None, None]:
    yield ShortLinkResponse(original_url=original_url, key_string=key_string)


@pytest.fixture
def random_filename() -> Generator[str, None, None]:
    yield f"{datetime.now().strftime('%y%m%d_%H%M%S')}-{uuid.uuid4().hex}-test.txt"


@pytest.fixture
def sqlite_url() -> Generator[str, None, None]:
    yield "sqlite:///:memory:"


@pytest.fixture
def unsupported_url() -> Generator[str, None, None]:
    yield "UNSUPPORTED:///:memory:"


@pytest.fixture
def db_url(db_scheme: str, db_username: str, db_password: str, db_hostname: str, db_port: str,
           db_path: str, db_query_params: str) -> Generator[str, None, None]:
    yield f"{db_scheme}://{db_username}:{db_password}@{db_hostname}:{db_port}{db_path}?{db_query_params}"


@pytest.fixture
def db_scheme() -> Generator[str, None, None]:
    yield "postgresql+psycopg2"


@pytest.fixture
def db_username() -> Generator[str, None, None]:
    yield "sl-service-account"


@pytest.fixture
def db_password() -> Generator[str, None, None]:
    yield "sl-service-account-secret"


@pytest.fixture
def db_port() -> Generator[str, None, None]:
    yield "5432"


@pytest.fixture
def db_hostname() -> Generator[str, None, None]:
    yield "localhost"


@pytest.fixture
def db_path() -> Generator[str, None, None]:
    yield "/sl_db"


@pytest.fixture
def db_query_params() -> Generator[str, None, None]:
    yield "a=b,c=d"


@pytest.fixture
def connect_args() -> Generator[str, None, None]:
    yield {"check_same_thread": False}
