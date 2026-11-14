from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

USUARIO_VALIDO = "standard_user"
CLAVE = "secret_sauce"


# Verifica que el usuario pueda cerrar sesión correctamente.
def test_logout(driver):
    login_page = LoginPage(driver).abrir()
    login_page.login_completo(USUARIO_VALIDO, CLAVE)
    inventario_page = InventoryPage(driver)

    # Cerrar sesión desde el menú lateral
    login_page_tras_logout = inventario_page.hacer_logout()

    # Verificar que volvimos a la página de login
    assert driver.current_url == LoginPage.URL
