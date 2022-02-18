from functools import lru_cache
from typing import Generator

from redis.client import Redis
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session

from settings.database import DatabaseConfiguration
from src.services import ConversionService, EncodingConfig, DecodingConfig, EncodingService, DecodingService
from src.settings import ConversionBase
from src.settings.caching import ShortLinkCache
from src.settings.settings import Settings


@lru_cache()
def get_settings() -> Settings:
    return Settings()


@lru_cache()
def get_engine() -> Engine:
    return get_settings().database_config.create_engine()


@lru_cache()
def get_session_maker() -> sessionmaker:
    return DatabaseConfiguration.create_session_maker(engine=get_engine())


def get_db() -> Generator[Session, None, None]:
    session_class: sessionmaker = get_session_maker()
    db: Session = session_class()
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


@lru_cache()
def get_short_link_cache() -> ShortLinkCache:
    redis_client: Redis = Redis.from_url(url=get_settings().caching_config.redis_url)
    return ShortLinkCache(redis_client)
