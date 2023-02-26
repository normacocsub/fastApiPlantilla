from fastapi.testclient import TestClient

from ..main import app


client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users/",
        json={
            "name": "John Doe",
            "email": "johndoe@example.com",
            "password": "supersecret"
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "johndoe@example.com"


def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "johndoe@example.com"


def test_update_user():
    response = client.put(
        "/users/1",
        json={
            "name": "Jane Doe",
            "email": "janedoe@example.com",
            "password": "supersecret"
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "janedoe@example.com"


def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted"}