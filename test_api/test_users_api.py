import pytest
import requests

from utils.logger import logger

CAMPOS_USUARIO = {"id", "email", "first_name", "last_name", "avatar"}


@pytest.mark.api
@pytest.mark.smoke
def test_get_users_page_1(reqres_url):
    logger.info("Consultando usuarios de la página 1")
    response = requests.get(reqres_url("/users?page=1"), timeout=10)

    assert response.status_code == 200
    logger.info("GET /users respondió con status=%s", response.status_code)
    assert "application/json" in response.headers.get("Content-Type", "")

    body = response.json()
    assert body["page"] == 1
    assert len(body["data"]) > 0

    for usuario in body["data"]:
        assert CAMPOS_USUARIO <= set(usuario.keys())
        assert usuario["email"].endswith("@reqres.in")
        assert usuario["id"] > 0
        assert usuario["first_name"]
        assert usuario["last_name"]
        assert usuario["avatar"].endswith(".jpg")

    assert response.elapsed.total_seconds() < 2
