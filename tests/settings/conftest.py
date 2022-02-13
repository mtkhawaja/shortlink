import tempfile
from typing import Generator

import pytest


@pytest.fixture
def log_level() -> Generator[str, None, None]:
    yield "INFO"


@pytest.fixture
def log_format() -> Generator[str, None, None]:
    yield "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


@pytest.fixture
def log_file() -> Generator[str, None, None]:
    yield tempfile.NamedTemporaryFile(mode="w").name
