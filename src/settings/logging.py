import logging
import pathlib
import sys

from pydantic import Field, BaseSettings


class LoggingConfiguration(BaseSettings):
    log_file: pathlib.Path = Field(
        default=None,
        env="LOG_FILE",
        description="Absolute path to log file. e.g. /var/log/short-link/application.log"
    )
    log_level: str = Field(
        default="INFO",
        env="LOG_LEVEL",
        description="Levels: ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']"
    )
    log_format: str = Field(
        default="%(asctime)s - [%(name)s] - [%(levelname)s] - %(message)s",
        env="LOG_FORMAT",
        description="Log msg format. With the default, formatting, a message may look like: "
                    "2022-02-13 13:53:13,463 - [src.main] - [INFO] - Application started. "
                    "See https://docs.python.org/3/howto/logging.html#formatters for more information.")
    ff_console_logging: bool = Field(
        default=True,
        env="FF_CONSOLE_LOGGING",
        description="If set to true, logs will be directed to console."
    )

    def configure_logging(self):
        LoggingConfiguration._create_log_file(self.log_file)
        handlers: list[logging.Handler] = self.create_log_handlers(self.log_level, self.log_file,
                                                                   self.log_format, self.ff_console_logging)
        logging.basicConfig(format=self.log_format, level=self.log_level, handlers=handlers)

    @staticmethod
    def _create_log_file(log_file: pathlib.Path):
        if log_file is not None and not log_file.exists():
            log_file.parents[0].mkdir(parents=True, exist_ok=True)

    @staticmethod
    def create_log_handlers(log_level: str, log_file: [pathlib.Path, None], log_format: str,
                            enable_console_logging: bool) -> list[logging.Handler]:
        handlers: list[logging.Handler] = []
        if enable_console_logging:
            handlers.append(LoggingConfiguration._create_console_handler(sys.stdout, log_level, log_format))
        if log_file:
            handlers.append(logging.FileHandler(log_file))
        if not enable_console_logging and log_file is None:
            handlers.append(logging.NullHandler())
        return handlers

    @staticmethod
    def _create_console_handler(stream, log_level: str, log_format: str) -> logging.StreamHandler:
        stream_handler = logging.StreamHandler(stream)
        stream_handler.setFormatter(logging.Formatter(log_format))
        stream_handler.setLevel(log_level)
        return stream_handler

    @staticmethod
    def _create_console_logger(logger_name: str, stream_handler: logging.StreamHandler) -> logging.Logger:
        logger = logging.getLogger(logger_name)
        logger.addHandler(stream_handler)
        return logger

    def log_logging_configuration(self, logger: logging.Logger) -> None:
        logger.info(f"Log level set to: '{self.log_level}'")
        if self.ff_console_logging:
            logger.info("`FF_CONSOLE_LOGGING` is set to 'true'. Logs will be directed to console.")
        if self.log_file:
            logger.info(f"Log file set to: '{self.log_file}'")
        else:
            logger.info("Log file not set.")
        if not self.ff_console_logging and self.log_file is None:
            print("Log file ('LOG_FILE=None') not set and "
                  "console logging ('FF_CONSOLE_LOGGING=False') is disabled. "
                  "No application logs will be generated.")
