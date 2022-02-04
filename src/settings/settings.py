from pydantic import (
    BaseSettings,
    Field,
)

from src.settings.constants import ConversionBase, Environment


class Settings(BaseSettings):
    environment: Environment = Field(default=Environment.DEV, env="ENVIRONMENT")
    conversion_base: ConversionBase = Field(default=ConversionBase.BASE_64, env="CONVERSION_BASE")
