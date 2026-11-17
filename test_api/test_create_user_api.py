from datetime import datetime

import pytest
import requests

CASOS_USUARIO = [
    ("Luis Romero", "QA Automation"),
    ("Ana Perez", "Developer"),
    ("Carlos Diaz", "Product Owner"),
]


@pytest.mark.api
@pytest.mark.parametrize("nombre, trabajo", CASOS_USUARIO)
def test_create_user_api(reqres_url, nombre, trabajo):
    payload = {"name": nombre, "job": trabajo}

    response = requests.post(reqres_url("/users"), json=payload, timeout=10)

    assert response.status_code == 201
    assert "application/json" in response.headers.get("Content-Type", "")

    body = response.json()
    assert body["name"] == nombre
    assert body["job"] == trabajo
    assert "id" in body
    assert "createdAt" in body
    assert str(datetime.now().year) in body["createdAt"]

    assert response.elapsed.total_seconds() < 2
