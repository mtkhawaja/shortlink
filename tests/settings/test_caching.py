from unittest.mock import Mock

from src.db.schemas.short_link_schemas import ShortLinkResponse
from src.settings.caching import CachingConfiguration, ShortLinkCache


class TestCaching:

    def test_should_cache_write_with_name_space_prefixed_when_caching_a_short_link_write(
            self, mock_redis_client: Mock, short_link_response: ShortLinkResponse
    ):
        caching_layer = ShortLinkCache(mock_redis_client)
        caching_layer.cache_write(short_link_response)
        original_url_cache_key = f"{caching_layer.original_url_ns}:{short_link_response.original_url}"
        assert mock_redis_client.set.called
        mock_redis_client.set.assert_called_with(original_url_cache_key, short_link_response.key_string)

    def test_should_return_none_when_retrieving_a_write_that_is_not_cached(
            self, mock_redis_client: Mock, original_url: str
    ):
        mock_redis_client.get.return_value = None
        caching_layer = ShortLinkCache(mock_redis_client)
        response = caching_layer.retrieve_write(original_url)
        assert response is None

    def test_should_retrieve_write_using_name_space_prefixed_key_when_retrieving_a_cached_write(
            self, mock_redis_client: Mock, original_url: str, key_string: str
    ):
        mock_redis_client.get.return_value = key_string
        caching_layer = ShortLinkCache(mock_redis_client)
        original_url_cache_key: str = f"{caching_layer.original_url_ns}:{original_url}"
        response = caching_layer.retrieve_write(original_url)
        assert response is not None
        assert response.original_url == original_url
        assert response.key_string == key_string
        assert mock_redis_client.get.called
        mock_redis_client.get.assert_called_with(original_url_cache_key)

    def test_should_cache_read_with_name_space_prefixed_when_caching_a_short_link_read(
            self, mock_redis_client: Mock, short_link_response: ShortLinkResponse
    ):
        caching_layer = ShortLinkCache(mock_redis_client)
        key_string_cache_key = f"{caching_layer.key_string_ns}:{short_link_response.key_string}"
        caching_layer.cache_read(short_link_response)
        assert mock_redis_client.set.called
        mock_redis_client.set.assert_called_with(key_string_cache_key, short_link_response.original_url)

    def test_should_return_none_when_retrieving_a_read_that_is_not_cached(
            self, mock_redis_client: Mock, key_string: str
    ):
        mock_redis_client.get.return_value = None
        caching_layer = ShortLinkCache(mock_redis_client)
        response = caching_layer.retrieve_read(key_string)
        assert response is None

    def test_should_retrieve_read_using_name_space_prefixed_key_when_retrieving_a_cached_read(
            self, mock_redis_client: Mock, original_url: str, key_string: str
    ):
        mock_redis_client.get.return_value = original_url
        caching_layer = ShortLinkCache(mock_redis_client)
        key_string_cache_key: str = f"{caching_layer.key_string_ns}:{key_string}"
        response = caching_layer.retrieve_read(key_string)
        assert response is not None
        assert response.original_url == original_url
        assert response.key_string == key_string
        assert mock_redis_client.get.called
        mock_redis_client.get.assert_called_with(key_string_cache_key)

    def test_should_create_redis_url_when_a_redis_url_is_not_explicitly_set(
            self, redis_user, redis_port, redis_password, redis_host, monkeypatch):
        monkeypatch.setenv('REDIS_USER', redis_user)
        monkeypatch.setenv('REDIS_PASSWORD', redis_password)
        monkeypatch.setenv('REDIS_HOST', redis_host)
        monkeypatch.setenv('REDIS_PORT', redis_port)
        caching_config = CachingConfiguration()
        expected_url = f"redis://{redis_user}:{redis_password}@{redis_host}:{redis_port}"
        assert caching_config.redis_url == expected_url

    def test_should_sync_properties_with_redis_url_when_a_redis_url_is_explicitly_set(
            self, redis_user, redis_port, redis_password, redis_host, monkeypatch):
        monkeypatch.setenv('REDIS_URL', f"redis://{redis_user}:{redis_password}@{redis_host}:{redis_port}")
        monkeypatch.setenv('REDIS_USER', "GARBAGE_VALUE")
        caching_config = CachingConfiguration()
        assert caching_config.redis_user == redis_user
        assert caching_config.redis_password == redis_password
        assert caching_config.redis_port == redis_port
        assert caching_config.redis_host == redis_host
