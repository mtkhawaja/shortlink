import logging
import pathlib
import tempfile
from pathlib import Path

from src.settings.logging import LoggingConfiguration


class TestLoggingConfiguration:

    def test_should_create_log_file_when_configured_log_file_and_parent_directories_do_not_exist(
            self, random_filename: str
    ):
        temp_dir = Path(tempfile.gettempdir())
        log_file = temp_dir / random_filename
        logging_configuration = LoggingConfiguration(log_file=log_file)
        logging_configuration.configure_logging()
        assert Path(log_file).is_file()

    def test_should_use_null_handler_for_logging_when_console_logging_is_disabled_and_a_log_file_is_not_provided(
            self, log_level: str, log_format: str
    ):
        handlers = LoggingConfiguration.create_log_handlers(log_level=log_level, log_format=log_format,
                                                            log_file=None, enable_console_logging=False)
        assert handlers is not None
        assert len(handlers) == 1
        assert isinstance(handlers[0], logging.NullHandler)

    def test_should_use_stream_handler_for_logging_when_console_logging_is_enabled(
            self, log_level: str, log_format: str
    ):
        handlers = LoggingConfiguration.create_log_handlers(log_level=log_level, log_format=log_format,
                                                            log_file=None, enable_console_logging=True)
        assert handlers is not None
        assert len(handlers) == 1
        stream_handler = handlers[0]
        assert isinstance(stream_handler, logging.StreamHandler)
        assert stream_handler.level == logging.getLevelName(log_level)

    def test_should_use_file_handler_for_logging_when_a_log_file_is_defined(
            self, log_level: str, log_format: str, log_file: str
    ):
        handlers = LoggingConfiguration.create_log_handlers(log_level=log_level, log_format=log_format,
                                                            log_file=pathlib.Path(log_file),
                                                            enable_console_logging=False)
        assert handlers is not None
        assert len(handlers) == 1
        file_handler = handlers[0]
        assert isinstance(file_handler, logging.FileHandler)
        assert file_handler.baseFilename == log_file

    def test_should_use_both_a_file_handler_and_a_stream_handler_when_console_logging_is_enabled_and_a_log_file_is_set(
            self, log_level: str, log_format: str, log_file: str
    ):
        handlers = LoggingConfiguration.create_log_handlers(log_level=log_level, log_format=log_format,
                                                            log_file=pathlib.Path(log_file),
                                                            enable_console_logging=True)
        assert handlers is not None
        assert len(handlers) == 2
