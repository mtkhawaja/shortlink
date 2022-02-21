from src.services import ConversionService
from src.settings.caching import NullShortLinkCache, ShortLinkCache
from src.settings.dependencies import get_conversion_service, get_settings, get_db, get_short_link_cache
from src.settings.settings import Settings


class TestDependencies:

    def test_should_load_settings_when_loading_settings_as_a_dependency(self):
        get_settings.cache_clear()
        settings: Settings = get_settings()
        assert settings is not None

    def test_should_load_conversion_service_when_loading_conversion_service_as_a_dependency(self):
        get_settings.cache_clear()
        settings: Settings = get_settings()
        get_conversion_service(settings.conversion_base)
        conversion_service: ConversionService = get_conversion_service(settings.conversion_base)
        assert conversion_service is not None
        assert conversion_service.base == settings.conversion_base

    def test_should_load_db_when_loading_db_as_a_dependency(self):
        get_settings.cache_clear()
        settings = get_settings()
        settings.database_config.db_url = "sqlite:///:memory:"
        assert next(get_db()) is not None

    def test_should_load_no_op_short_link_cache_when_caching_is_disabled(self):
        get_settings.cache_clear()
        get_short_link_cache.cache_clear()
        settings: Settings = get_settings()
        settings.caching_config.ff_caching = False
        get_short_link_cache.cache_clear()
        cache = get_short_link_cache()
        assert cache is not None
        assert isinstance(cache, NullShortLinkCache)

    def test_should_load_short_link_cache_when_caching_is_enabled(self):
        get_settings.cache_clear()
        get_short_link_cache.cache_clear()
        settings = get_settings()
        settings.caching_config.ff_caching = True
        cache = get_short_link_cache()
        assert cache is not None
        assert not isinstance(cache, NullShortLinkCache)
        assert isinstance(cache, ShortLinkCache)
