from app.core.config import PROJECT_NAME


def test_read_main(client):
    response = client.get("/api/v1")
    assert response.status_code == 200
    assert response.json() == {"message": f"Welcome to {PROJECT_NAME} !"}
