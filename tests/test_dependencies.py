from src.services import ConversionService
from src.settings.dependencies import get_conversion_service, get_settings
from src.settings.settings import Settings


class TestDependencies:

    def test_should_load_settings_when_loading_settings_as_a_dependency(self):
        settings: Settings = get_settings()
        assert settings is not None

    def test_should_load_conversion_service_when_loading_conversion_service_as_a_dependency(self):
        settings: Settings = get_settings()
        get_conversion_service(settings.conversion_base)
        conversion_service: ConversionService = get_conversion_service(settings.conversion_base)
        assert conversion_service is not None
        assert conversion_service.base == settings.conversion_base
