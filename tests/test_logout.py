from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

USUARIO_VALIDO = "standard_user"
CLAVE = "secret_sauce"


# Verifica que el usuario pueda cerrar sesión correctamente.
def test_logout(driver):
    logger.info("Iniciando test de cierre de sesión")
    login_page = LoginPage(driver).abrir()
    login_page.login_completo(USUARIO_VALIDO, CLAVE)
    inventario_page = InventoryPage(driver)

    # Cerrar sesión desde el menú lateral
    login_page_tras_logout = inventario_page.hacer_logout()

    # Verificar que volvimos a la página de login
    assert driver.current_url == LoginPage.URL
    logger.info("Logout exitoso, URL actual: %s", driver.current_url)
