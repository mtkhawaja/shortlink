import http

import pytest
import requests
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool

from src.main import app
from src.settings.caching import ShortLinkCache, NullShortLinkCache
from src.settings.database import Base
from src.settings.dependencies import get_short_link_cache, get_db

client = TestClient(app)

engine = create_engine(f'sqlite:///:memory:',
                       connect_args={'check_same_thread': False},
                       poolclass=StaticPool)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def setup_and_teardown_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def override_get_db() -> Session:
    db = None
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def cache_override() -> ShortLinkCache:
    return NullShortLinkCache()


app.dependency_overrides[get_short_link_cache] = cache_override
app.dependency_overrides[get_db] = override_get_db


class TestShortLinkRoutes:

    def test_should_create_short_link_when_a_post_request_is_made_to_the_create_end_point(self, request_body: dict,
                                                                                          setup_and_teardown_db):
        response: requests.Response = client.post("/v1/create/", json=request_body)
        assert response is not None
        assert response.status_code == http.HTTPStatus.OK, f"'{response.url}' not successful."

    def test_should_retrieve_original_url_when_a_get_request_is_made_to_the_resolve_end_point_with_a_key_string(
            self, request_body: dict, setup_and_teardown_db
    ):
        creation_response = client.post("/v1/create/", json=request_body, )
        assert creation_response is not None
        assert creation_response.status_code == http.HTTPStatus.OK
        key_str = creation_response.json()["key_string"]
        retrieval_response = client.get(f"/v1/resolve/{key_str}")
        assert retrieval_response is not None
        assert retrieval_response.status_code == http.HTTPStatus.OK
        assert retrieval_response.json()["original_url"] == request_body["original_url"]
