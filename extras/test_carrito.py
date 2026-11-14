from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.funciones_saucedemo import take_screenshot

USUARIO_VALIDO = "standard_user"
CLAVE = "secret_sauce"


# Verifica que un usuario pueda agregar un producto al carrito y que este se actualice correctamente. (ACTIVIDAD 3)
def test_carrito(driver):
    login_page = LoginPage(driver).abrir()

    # Inicia sesión con credenciales válidas
    login_page.login_completo(USUARIO_VALIDO, CLAVE)
    inventario_page = InventoryPage(driver)

    # Agregar el primer producto al carrito
    inventario_page.agregar_primer_producto()

    # Verificar que el carrito tenga 1 artículo
    assert inventario_page.obtener_contador_carrito() == 1
    print('Carrito actualizado correctamente con 1 artículo.')

    # Navegar al carrito y verificar que el producto esté presente
    cart_page = inventario_page.ir_al_carrito()
    take_screenshot(driver, "captura4.png")

    nombres = cart_page.obtener_nombres_productos()
    assert "Sauce Labs Backpack" in nombres
    print(f'Producto en carrito: {nombres[0]}')
