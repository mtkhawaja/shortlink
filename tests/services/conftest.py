from typing import Generator

import pytest

from src.services import BaseDecodingService, DecodingConfig, DecodingService, BaseEncodingService, EncodingConfig, \
    EncodingService
from src.services.conversion_service import ConversionService, BaseConversionService
from src.settings import ConversionBase


@pytest.fixture
def binary_decoder() -> Generator[BaseDecodingService, None, None]:
    config = DecodingConfig(ConversionBase.BINARY, ConversionBase.BINARY.alphabet_map)
    yield DecodingService(config)


@pytest.fixture
def octal_decoder() -> Generator[BaseDecodingService, None, None]:
    config = DecodingConfig(ConversionBase.OCTAL, ConversionBase.OCTAL.alphabet_map)
    yield DecodingService(config)


@pytest.fixture
def decimal_decoder() -> Generator[BaseDecodingService, None, None]:
    config = DecodingConfig(ConversionBase.DECIMAL, ConversionBase.DECIMAL.alphabet_map)
    yield DecodingService(config)


@pytest.fixture
def hex_decoder() -> Generator[BaseDecodingService, None, None]:
    config = DecodingConfig(ConversionBase.HEX, ConversionBase.HEX.alphabet_map)
    yield DecodingService(config)


@pytest.fixture
def base_32_decoder() -> Generator[BaseDecodingService, None, None]:
    config = DecodingConfig(ConversionBase.BASE_32, ConversionBase.BASE_32.alphabet_map)
    yield DecodingService(config)


@pytest.fixture
def base_64_decoder() -> Generator[BaseDecodingService, None, None]:
    config = DecodingConfig(ConversionBase.BASE_64, ConversionBase.BASE_64.alphabet_map)
    yield DecodingService(config)


@pytest.fixture
def binary_encoder() -> Generator[BaseEncodingService, None, None]:
    config = EncodingConfig(ConversionBase.BINARY, ConversionBase.BINARY.alphabet)
    yield EncodingService(config)


@pytest.fixture
def octal_encoder() -> Generator[BaseEncodingService, None, None]:
    config = EncodingConfig(ConversionBase.OCTAL, ConversionBase.OCTAL.alphabet)
    yield EncodingService(config)


@pytest.fixture
def decimal_encoder() -> Generator[BaseEncodingService, None, None]:
    config = EncodingConfig(ConversionBase.DECIMAL, ConversionBase.DECIMAL.alphabet)
    yield EncodingService(config)


@pytest.fixture
def hex_encoder() -> Generator[BaseEncodingService, None, None]:
    config = EncodingConfig(ConversionBase.HEX, ConversionBase.HEX.alphabet)
    yield EncodingService(config)


@pytest.fixture
def base_32_encoder() -> Generator[BaseEncodingService, None, None]:
    config = EncodingConfig(ConversionBase.BASE_32, ConversionBase.BASE_32.alphabet)
    yield EncodingService(config)


@pytest.fixture
def base_64_encoder() -> Generator[BaseEncodingService, None, None]:
    config = EncodingConfig(ConversionBase.BASE_64, ConversionBase.BASE_64.alphabet)
    yield EncodingService(config)


@pytest.fixture
def base_64_conversion_service(
        base_64_encoder: BaseEncodingService, base_64_decoder: BaseDecodingService
) -> Generator[BaseConversionService, None, None]:
    yield ConversionService(base_64_encoder, base_64_decoder)
