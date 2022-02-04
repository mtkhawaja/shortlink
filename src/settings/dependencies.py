from functools import lru_cache

from src.services import ConversionService, EncodingConfig, DecodingConfig, EncodingService, DecodingService
from src.settings import ConversionBase
from src.settings.database import SessionLocal
from src.settings.settings import Settings


@lru_cache()
def get_settings() -> Settings:
    return Settings()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_conversion_service(conversion_base: ConversionBase) -> ConversionService:
    encoding_config = EncodingConfig(conversion_base, conversion_base.alphabet)
    decoding_config = DecodingConfig(conversion_base, conversion_base.alphabet_map)
    encoding_service = EncodingService(encoding_config)
    decoding_service = DecodingService(decoding_config)
    return ConversionService(encoding_service, decoding_service)
