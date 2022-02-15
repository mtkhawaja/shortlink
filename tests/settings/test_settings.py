from src.settings import Environment, ConversionBase
from src.settings.settings import Settings


class TestSettings:
    def test_should_use_dev_environment_when_an_explicit_environment_is_not_set(self):
        settings = Settings()
        assert settings.environment == Environment.DEV

    def test_should_use_base_64_when_an_explicit_conversion_base_is_not_set(self):
        settings = Settings()
        assert settings.conversion_base == ConversionBase.BASE_64

    def test_should_externalized_settings_when_settings_are_defined_in_the_environment(self, monkeypatch):
        monkeypatch.setenv('ENVIRONMENT', Environment.QA.name)
        monkeypatch.setenv('CONVERSION_BASE', str(ConversionBase.BASE_32.value))
        settings = Settings()
        assert settings.environment == Environment.QA
        assert settings.conversion_base == ConversionBase.BASE_32
