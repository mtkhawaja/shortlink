from logging import Logger
from typing import Any, Optional
from urllib.parse import urlparse, ParseResult

from pydantic import BaseSettings, Field
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

Base = declarative_base()


class DatabaseConfiguration(BaseSettings):
    _DEFAULT_SQLITE_URL = "sqlite:///:memory:"
    db_url: str = Field(
        default=None,
        env="DB_URL",
        description="Connection url for database based on the following template: "
                    "'<scheme>://<username>:<password>@<hostname>:<port>/<database>' "
                    "For example: 'postgresql+psycopg2://short-link:secret@localhost/sl_db'"
    )
    connect_args: dict = Field(
        default_factory=lambda: dict(),
        env="DB_CONNECT_ARGS",
        description="Arguments passed directly to the DBAPI’s connect() method See "
                    "'https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine.params.connect_args'"
                    " for more information",
    )
    use_in_memory_sqlite: bool = Field(
        default=False,
        env="USE_IN_MEMORY_SQLITE",
        description="Ignore all other database settings and use in memory sqlite."
    )
    scheme: Optional[str] = ""
    username: Optional[str] = ""
    password: Optional[str] = ""
    hostname: Optional[str] = ""
    port: Optional[str] = ""
    path: Optional[str] = ""
    query_params: Optional[str] = ""

    def __init__(self, **values: Any):
        super().__init__(**values)
        self._initialize_properties()

    def log_database_configuration(self, logger: Logger):
        if self.use_in_memory_sqlite:
            logger.warning(
                f"In-Memory SQLite db (db_url='{self.db_url}') configured as backend. "
                "User defined configuration will be overridden & state will be lost on shutdown!")
            return
        log_url: str = self.db_url.replace(self.password, '<redacted>') if self.password else self.db_url
        logger.info(f"Database Connection URL: '{log_url}'")

    def _initialize_properties(self) -> None:
        if self.use_in_memory_sqlite:
            self.db_url = self._DEFAULT_SQLITE_URL
            self.connect_args = {'check_same_thread': False}
        url: ParseResult = urlparse(self.db_url)
        self.scheme = url.scheme or ""
        self.username = url.username or ""
        self.password = url.password or ""
        self.port = str(url.port) if url.port else ""
        self.hostname = url.hostname or ""
        self.path = url.path or ""
        self.query_params = url.query or ""

    def create_engine(self):
        if self.use_in_memory_sqlite:
            return create_engine(self.db_url, connect_args=self.connect_args, poolclass=StaticPool)
        if self.db_url is None:
            raise ValueError("Database URL is None. One of the following "
                             "env vars must be set to create engine: ['DB_URL', 'USE_IN_MEMORY_SQLITE']")
        return create_engine(self.db_url, connect_args=self.connect_args)

    @staticmethod
    def create_session_maker(engine: Engine):
        return sessionmaker(autocommit=False, autoflush=False, bind=engine)
