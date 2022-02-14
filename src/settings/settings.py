import logging
from typing import Any

from pydantic import (
    BaseSettings,
    Field,
)

from src.settings.caching import CachingConfiguration
from src.settings.constants import ConversionBase, Environment
from src.settings.logging import LoggingConfiguration


class Settings(BaseSettings):
    environment: Environment = Field(default=Environment.DEV,
                                     env="ENVIRONMENT",
                                     description=f"Available options: ['DEV', 'QA', 'STG', 'PROD']")
    conversion_base: ConversionBase = Field(
        default=ConversionBase.BASE_64,
        env="CONVERSION_BASE",
        description="Conversion base for encoding/decoding key strings. Available options: ['2', '8', '16', '32', '64']"
    )

    logging_config: LoggingConfiguration = LoggingConfiguration()
    caching_config: CachingConfiguration = CachingConfiguration()

    def __init__(self, **values: Any):
        super().__init__(**values)
        self.logging_config.configure_logging()

    def log_configuration(self, logger: logging.Logger) -> None:
        logger.info(f"Environment: '{self.environment.name}'")
        logger.info(f"Conversion base: '{self.conversion_base}'")
        self.logging_config.log_logging_configuration(logger)
        self.caching_config.log_caching_configuration(logger)