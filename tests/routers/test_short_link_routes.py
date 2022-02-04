import http

import requests
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


class TestShortLinkRoutes:

    def test_should_create_short_link_when_a_post_request_is_made_to_the_create_end_point(self, request_body: dict):
        response: requests.Response = client.post("/v1/create/", json=request_body)
        assert response is not None
        assert response.status_code == http.HTTPStatus.OK, f"'{response.url}' not successful."

    def test_should_retrieve_original_url_when_a_get_request_is_made_to_the_resolve_end_point_with_a_key_string(
            self, request_body: dict
    ):
        creation_response = client.post("/v1/create/", json=request_body)
        key_str = creation_response.json()["key_string"]
        retrieval_response = client.get(f"/v1/resolve/{key_str}")
        assert retrieval_response is not None
        assert retrieval_response.status_code == http.HTTPStatus.OK
        assert retrieval_response.json()["original_url"] == request_body["original_url"]
