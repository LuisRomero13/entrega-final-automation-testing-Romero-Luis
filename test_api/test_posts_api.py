import pytest
import requests

from utils.logger import logger

POST_ID = 1
CAMPOS_POST = {"id", "title", "body", "userId"}


@pytest.mark.api
def test_put_post(jsonplaceholder_url):
    payload = {
        "id": POST_ID,
        "title": "Automation Testing Guide",
        "body": "Guía completa de testing automatizado",
        "userId": 1,
    }

    logger.info("Actualizando post %s con PUT", POST_ID)
    response = requests.put(
        jsonplaceholder_url(f"/posts/{POST_ID}"), json=payload, timeout=10
    )
    logger.info("PUT /posts/%s respondió con status=%s", POST_ID, response.status_code)

    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")

    body = response.json()
    assert CAMPOS_POST <= set(body.keys())
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["id"] == POST_ID

    assert response.elapsed.total_seconds() < 1.5


@pytest.mark.api
def test_patch_post(jsonplaceholder_url):
    payload = {"title": "Título actualizado por PATCH"}

    logger.info("Actualizando post %s con PATCH", POST_ID)
    response = requests.patch(
        jsonplaceholder_url(f"/posts/{POST_ID}"), json=payload, timeout=10
    )
    logger.info("PATCH /posts/%s respondió con status=%s", POST_ID, response.status_code)

    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")

    body = response.json()
    assert CAMPOS_POST <= set(body.keys())
    assert body["title"] == payload["title"]
    assert body["body"]
    assert body["userId"]

    assert response.elapsed.total_seconds() < 1


@pytest.mark.api
def test_delete_post(jsonplaceholder_url):
    logger.info("Eliminando post %s", POST_ID)
    response = requests.delete(
        jsonplaceholder_url(f"/posts/{POST_ID}"), timeout=10
    )
    logger.info("DELETE /posts/%s respondió con status=%s", POST_ID, response.status_code)

    assert response.status_code in (200, 204)
    if response.status_code == 200:
        assert response.json() == {}

    assert response.elapsed.total_seconds() < 1


@pytest.mark.api
def test_get_post_inexistente(jsonplaceholder_url):
    logger.info("Solicitando un post inexistente")
    response = requests.get(
        jsonplaceholder_url("/posts/999999"), timeout=10
    )
    logger.info("GET /posts/999999 respondió con status=%s", response.status_code)

    assert response.status_code == 404
