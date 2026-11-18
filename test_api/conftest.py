import uuid

import pytest
import requests

from utils.logger import logger

REQRES_BASE = "https://reqres.in/api"
JSONPLACEHOLDER_BASE = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="module")
def reqres_url():
    """Construye URLs del entorno de práctica reqres.in."""
    def construir_url(path):
        return f"{REQRES_BASE}{path}"

    return construir_url


@pytest.fixture(scope="module")
def jsonplaceholder_url():
    """Construye URLs del entorno de práctica JSONPlaceholder."""
    def construir_url(path):
        return f"{JSONPLACEHOLDER_BASE}{path}"

    return construir_url


@pytest.fixture(scope="module")
def created_post(jsonplaceholder_url):
    """Crea un post real y comparte sus datos con los tests encadenados."""
    payload = {
        "title": f"Post de prueba {uuid.uuid4().hex[:8]}",
        "body": "Contenido creado para el flujo CRUD",
        "userId": 1,
    }
    logger.info("Creando post temporal para el flujo CRUD")
    response = requests.post(jsonplaceholder_url("/posts"), json=payload, timeout=10)
    assert response.status_code == 201
    logger.info("Post creado con id=%s y status=%s", response.json().get("id"), response.status_code)
    return response.json()
