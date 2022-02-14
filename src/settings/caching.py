import logging
from typing import Any, Optional
from urllib.parse import urlparse

from pydantic import BaseSettings, Field
from redis.client import Redis

from src.db.schemas.short_link_schemas import ShortLinkResponse


class CachingConfiguration(BaseSettings):
    redis_user: str = Field(
        default="",
        env="REDIS_USER",
        description="Redis username. e.g. short-link-redis-client"
    )
    redis_password: str = Field(
        default="",
        env="REDIS_PASSWORD",
        description="Redis password. e.g. ^E05FNf8*NHqfR*xGIR"
    )
    redis_host: str = Field(
        default="",
        env="REDIS_HOST",
        description="Redis host name. e.g. redis.example.com"
    )
    redis_port: str = Field(
        default="6379",
        env="REDIS_PORT",
        description="Redis port. e.g 6379"
    )

    redis_url: str = Field(
        default=None,
        env="REDIS_URL",
        description="Redis connection string based on the following template: "
                    "'redis://<redis_user>:<self.redis_password>@<redis_host>:<self.redis_port>' "
                    "For example: 'redis://short-link-redis-client:^E05FNf8*NHqfR*xGIR@redis.example.com:6379' "
                    "Note: If `REDIS_URL` is set, all other redis configuration options are overridden"
    )

    def __init__(self, **values: Any):
        super().__init__(**values)
        self.redis_url = self._create_redis_url()

    def _create_redis_url(self):
        if self.redis_url:
            self._sync_properties()
            return self.redis_url
        return f"redis://{self.redis_user}:{self.redis_password}@{self.redis_host}:{self.redis_port}"

    def log_caching_configuration(self, logger):
        logger.info(f"Redis Url: {self.redis_url.replace(self.redis_password, '<redacted>')}")

    def _sync_properties(self):
        redis_url = urlparse(self.redis_url, scheme='redis')
        self.redis_host = redis_url.hostname
        self.redis_port = str(redis_url.port)
        self.redis_user = redis_url.username
        self.redis_password = redis_url.password


class ShortLinkCache(object):

    def __init__(self, redis_client: Redis, key_string_ns: str = None, original_url_ns: str = None) -> None:
        self._redis = redis_client
        self._key_string_ns = key_string_ns if key_string_ns else "key_str"
        self._original_url_ns = original_url_ns if original_url_ns else "orig_url"
        self._logger = logging.getLogger(__name__)

    def cache_write(self, response: ShortLinkResponse) -> None:
        ns_url: str = self._create_ns_key(self._original_url_ns, response.original_url)
        self._logger.debug(f"Caching 'write'. Response: {response}")
        self._redis.set(ns_url, response.key_string)

    def retrieve_write(self, original_url: str) -> Optional[ShortLinkResponse]:
        ns_url_key: str = self._create_ns_key(self._original_url_ns, original_url)
        cached_key_string = self._redis.get(ns_url_key)
        if not cached_key_string:
            self._logger.debug(f"Cache miss on 'write'. Original Url = '{original_url}'")
            return None
        response = ShortLinkResponse(original_url=original_url, key_string=cached_key_string)
        self._logger.debug(f"Cache hit on 'write'. Reusing response: '{response}'")
        return response

    def cache_read(self, response: ShortLinkResponse) -> None:
        ns_short_link_key: str = self._create_ns_key(self._key_string_ns, response.key_string)
        self._logger.debug(f"Caching 'read'. Response: {response}")
        return self._redis.set(ns_short_link_key, response.original_url)

    def retrieve_read(self, short_link_key_string: str) -> Optional[ShortLinkResponse]:
        ns_short_link_key: str = self._create_ns_key(self._key_string_ns, short_link_key_string)
        cached_original_url = self._redis.get(ns_short_link_key)
        if not cached_original_url:
            self._logger.debug(f"Cache miss on 'read'. Key String = '{short_link_key_string}'")
            return None
        response = ShortLinkResponse(original_url=cached_original_url, key_string=short_link_key_string)
        self._logger.debug(f"Cache hit on 'read'. Retrieved response: '{response}'")
        return response

    @property
    def key_string_ns(self):
        return self._key_string_ns

    @property
    def original_url_ns(self):
        return self._original_url_ns

    @staticmethod
    def _create_ns_key(ns: str, base_key: str) -> str:
        return f"{ns}:{base_key}"


class NullShortLinkCache(ShortLinkCache):
    def __init__(self, redis_client: Redis = None):
        super().__init__(redis_client)

    def cache_write(self, response: ShortLinkResponse) -> None:
        # nop
        pass

    def retrieve_write(self, original_url: str) -> Optional[ShortLinkResponse]:
        # nop
        return None

    def cache_read(self, response: ShortLinkResponse) -> None:
        # nop
        pass

    def retrieve_read(self, short_link_key_string: str) -> Optional[ShortLinkResponse]:
        # nop
        return None
