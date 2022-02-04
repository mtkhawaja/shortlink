from typing import Generator

import pytest


@pytest.fixture
def request_body(original_url: str) -> Generator[str, None, None]:
    yield {"original_url": original_url}


@pytest.fixture
def original_url() -> Generator[str, None, None]:
    yield "https://www.example.com"
