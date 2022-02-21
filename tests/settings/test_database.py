import pytest

from src.settings.database import DatabaseConfiguration


class TestDatabase:
    def test_should_initialize_all_available_properties_when_a_supported_database_url_is_provided(
            self, db_url: str, db_scheme: str, db_username: str, db_password: str, db_hostname: str, db_port: str,
            db_path: str, db_query_params: str, connect_args: dict
    ):
        db_config = DatabaseConfiguration(use_in_memory_sqlite=False, db_url=db_url, connect_args=connect_args)
        assert db_config.scheme == db_scheme
        assert db_config.username == db_username
        assert db_config.password == db_password
        assert db_config.hostname == db_hostname
        assert db_config.port == db_port
        assert db_config.path == db_path
        assert db_config.query_params == db_query_params
        assert db_config.connect_args is not None, "connect_args must not be 'None'"

    def test_should_override_properties_when_in_memory_sqlite_is_configured_as_the_db(
            self, db_url: str, db_scheme: str, db_username: str, db_password: str, db_hostname: str, db_port: str,
            db_path: str, db_query_params: str, connect_args: dict
    ):
        db_config = DatabaseConfiguration(db_url=db_url, connect_args=connect_args, use_in_memory_sqlite=True)
        assert db_config.scheme == "sqlite"
        assert db_config.connect_args == {'check_same_thread': False}
        assert db_config.db_url == "sqlite:///:memory:"

    def test_should_initialize_optional_properties_to_empty_string_when_they_are_not_available(self):
        db_config = DatabaseConfiguration(use_in_memory_sqlite=False, db_url="")
        assert db_config.scheme == ""
        assert db_config.username == ""
        assert db_config.password == ""
        assert db_config.hostname == ""
        assert db_config.port == ""
        assert db_config.path == ""
        assert db_config.query_params == ""
        assert db_config.connect_args is not None, "connect_args must not be 'None'"

    def test_should_raise_value_error_when_engine_creation_is_attempted_before_a_db_url_is_set(self):
        db_config = DatabaseConfiguration(use_in_memory_sqlite=False, db_url=None)
        with pytest.raises(ValueError):
            db_config.create_engine()
