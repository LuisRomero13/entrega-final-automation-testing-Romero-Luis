import pytest
import requests

from utils.logger import logger

TITULO_ACTUALIZADO = "Título actualizado por QA"


@pytest.mark.api
@pytest.mark.e2e
def test_ciclo_de_vida_post(jsonplaceholder_url, created_post):
    """POST -> PATCH -> DELETE usando el id real devuelto por el servidor."""
    post_id = created_post["id"]
    assert post_id
    logger.info("Iniciando ciclo de vida del post id=%s", post_id)

    patch_response = requests.patch(
        jsonplaceholder_url(f"/posts/{post_id}"),
        json={"title": TITULO_ACTUALIZADO},
        timeout=10,
    )
    assert patch_response.status_code == 200
    logger.info("PATCH exitoso con status=%s", patch_response.status_code)
    assert "application/json" in patch_response.headers.get("Content-Type", "")

    post_actualizado = patch_response.json()
    assert isinstance(post_actualizado, dict)
    assert post_actualizado["title"] == TITULO_ACTUALIZADO

    delete_response = requests.delete(
        jsonplaceholder_url(f"/posts/{post_id}"), timeout=10
    )
    assert delete_response.status_code == 200
    logger.info("DELETE exitoso con status=%s", delete_response.status_code)
    assert delete_response.json() == {}

    tiempo_total = (
        patch_response.elapsed.total_seconds()
        + delete_response.elapsed.total_seconds()
    )
    assert tiempo_total < 3
