import base64
import html
import pathlib

import pytest
import pytest_html
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.funciones_saucedemo import opciones_chrome, tomar_captura_fallo
from utils.logger import logger

USUARIO_VALIDO = "standard_user"
CLAVE = "secret_sauce"

# Carpeta donde se guardan las capturas de los tests UI fallidos
TARGET = pathlib.Path("reports/screens")
TARGET.mkdir(parents=True, exist_ok=True)


@pytest.fixture(scope="function")
def driver():
    """Fixture que proporciona un WebDriver configurado."""
    logger.info("Iniciando WebDriver de Chrome")
    opciones, servicio = opciones_chrome()
    navegador = webdriver.Chrome(service=servicio, options=opciones)
    navegador.implicitly_wait(5)

    yield navegador

    logger.info("Cerrando WebDriver de Chrome")
    navegador.quit()


@pytest.fixture
def usuario_logueado(driver):
    """Fixture que realiza login antes de cada test que necesite el inventario."""
    login_page = LoginPage(driver).abrir()
    login_page.login_completo(USUARIO_VALIDO, CLAVE)
    return InventoryPage(driver)


def pytest_html_report_title(report):
    """Personaliza el título del reporte HTML."""
    report.title = "SauceDemo + API - Resumen de ejecución"


def pytest_html_results_summary(prefix, summary, postfix, session):
    """Agrega una descripción breve debajo del título del reporte."""
    prefix.extend(
        ["<p>Suite UI (Selenium) + API (Requests) con capturas y logging</p>"]
    )


def pytest_runtest_setup(item):
    """Registra el inicio de cada test en el log de la suite."""
    logger.info("INICIO test: %s", item.nodeid)


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura los fallos UI y adjunta la imagen al reporte HTML."""
    reporte = yield

    if reporte.when == "call":
        logger.info(
            "FIN test: %s -> %s (%.2fs)",
            item.nodeid,
            reporte.outcome,
            reporte.duration,
        )

    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            ruta = tomar_captura_fallo(driver, item.name)
            if ruta is not None:
                contenido = base64.b64encode(ruta.read_bytes()).decode("ascii")
                reporte.extras = getattr(reporte, "extras", [])
                reporte.extras.append(
                    pytest_html.extras.image(
                        contenido, name=item.name, extension="png"
                    )
                )
            logger.error("Test fallido: %s", item.nodeid)

    driver = item.funcargs.get("driver")
    if driver is not None:
        try:
            reporte.page_url = driver.current_url
        except Exception:
            reporte.page_url = "-"

    return reporte


def pytest_html_results_table_header(cells):
    """Añade una columna 'URL' al reporte HTML."""
    cells.insert(2, '<th class="sortable" data-column-type="url">URL</th>')


def pytest_html_results_table_row(report, cells):
    """Completa la columna 'URL' con la última URL visitada por el test."""
    url = html.escape(getattr(report, "page_url", "-"))
    cells.insert(2, f'<td class="col-url">{url}</td>')
