import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.datos import leer_csv_login

CASOS_LOGIN = leer_csv_login()


# Test parametrizado que verifica el login con datos del CSV
@pytest.mark.parametrize(
    "usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN
)
def test_login_desde_csv(driver, usuario, clave, debe_funcionar, descripcion):
    print(f'Caso: {descripcion}')

    login_page = LoginPage(driver).abrir()
    login_page.login_completo(usuario, clave)

    if debe_funcionar:
        # Si debe funcionar, verificamos que llegamos al inventario
        InventoryPage(driver)
        assert "/inventory.html" in driver.current_url
    else:
        # Si no debe funcionar, verificamos que hay un mensaje de error
        assert login_page.esta_error_visible()
        print('Mensaje de error:', login_page.obtener_mensaje_error())


# Test de smoke para verificar que al menos un login funciona
@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    login_page = LoginPage(driver).abrir()
    login_page.login_completo("standard_user", "secret_sauce")
    assert "/inventory.html" in driver.current_url
