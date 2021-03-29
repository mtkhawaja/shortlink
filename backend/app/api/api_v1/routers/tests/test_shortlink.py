from fastapi.testclient import TestClient
from starlette import responses
from app.db.models.Shortlink import Shortlink


def create_shortlink(client: TestClient, url="https://example.com"):
    response = client.post(
        "/api/v1/shortlink",
        json={"original_url": url},
    )
    return response


def test_shortlink_creation(client: TestClient):
    for primary_key in range(1, 101):
        response = create_shortlink(client)
        assert response.status_code == 200
        assert Shortlink.decode(response.json()["key_str"]) == primary_key


def test_original_link_retrieval_when_entry_exists(client: TestClient):
    original_url = "https://example.com/2131312131"
    sl = create_shortlink(client, original_url).json()
    response = client.get(f"/api/v1/shortlink/{sl['key_str']}")
    assert response.status_code == 200
    assert response.json()["original_url"] == original_url


def test_original_link_retrieval_when_entry_does_not_exist(client: TestClient):
    key_str = "Asd2w1~"
    response = client.get(f"/api/vi/shortlink/{key_str}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
