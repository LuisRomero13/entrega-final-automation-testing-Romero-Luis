import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.funciones_saucedemo import opciones_chrome, tomar_captura_fallo

USUARIO_VALIDO = "standard_user"
CLAVE = "secret_sauce"


@pytest.fixture(scope="function")
def driver():
    """Fixture que proporciona un WebDriver configurado."""
    opciones, servicio = opciones_chrome()
    navegador = webdriver.Chrome(service=servicio, options=opciones)
    navegador.implicitly_wait(5)

    yield navegador

    navegador.quit()


@pytest.fixture
def usuario_logueado(driver):
    """Fixture que realiza login antes de cada test que necesite el inventario."""
    login_page = LoginPage(driver).abrir()
    login_page.login_completo(USUARIO_VALIDO, CLAVE)
    return InventoryPage(driver)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Captura un screenshot automáticamente cuando un test falla."""
    resultado = yield
    reporte = resultado.get_result()
    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")
        if driver:
            tomar_captura_fallo(driver, item.name)
