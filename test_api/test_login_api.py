import pytest
import requests

from utils.logger import logger

CASOS_LOGIN = [
    ("eve.holt@reqres.in", "cityslicka", 200, True, "Credenciales válidas"),
    ("eve.holt@reqres.in", None, 400, False, "Email sin password"),
    (
        "usuario.invalido@reqres.in",
        "clave-incorrecta",
        400,
        False,
        "Usuario inexistente",
    ),
]


@pytest.mark.api
@pytest.mark.parametrize(
    "email, password, status_esperado, espera_token, descripcion",
    CASOS_LOGIN,
    ids=[caso[4] for caso in CASOS_LOGIN],
)
def test_login_api(
    reqres_url, email, password, status_esperado, espera_token, descripcion
):
    logger.info("Ejecutando caso de login API: %s", descripcion)
    payload = {"email": email}
    if password is not None:
        payload["password"] = password

    response = requests.post(reqres_url("/login"), json=payload, timeout=10)
    logger.info("POST /login respondió con status=%s", response.status_code)

    assert response.status_code == status_esperado
    assert "application/json" in response.headers.get("Content-Type", "")

    body = response.json()
    if espera_token:
        assert "token" in body
        assert body["token"]
    else:
        assert "error" in body

    assert response.elapsed.total_seconds() < 2
