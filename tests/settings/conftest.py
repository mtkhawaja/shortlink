import tempfile
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
