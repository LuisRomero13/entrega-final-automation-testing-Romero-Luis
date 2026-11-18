from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

USUARIO_VALIDO = "standard_user"
CLAVE = "secret_sauce"


# Verifica que el catálogo de productos se muestre correctamente. (ACTIVIDAD 2)
def test_catalogo_y_elementos(driver):
    logger.info("Verificando catálogo y elementos de la interfaz")
    login_page = LoginPage(driver).abrir()

    # Inicia sesión con credenciales válidas
    login_page.login_completo(USUARIO_VALIDO, CLAVE)
    inventario_page = InventoryPage(driver)

    # Verificar que existan productos visibles
    productos = inventario_page.obtener_productos()
    assert len(productos) > 0
    logger.info("Se encontraron %s productos en el catálogo", len(productos))

    # Obtener nombre y precio del primer producto
    nombre, precio = inventario_page.obtener_primer_producto()
    logger.info("Primer producto: %s - Precio: %s", nombre, precio)
    assert nombre != ""
    assert precio != ""

    # Verificar elementos importantes de la interfaz
    assert inventario_page.elemento_interfaz_visible("menu")
    assert inventario_page.elemento_interfaz_visible("filtro")
    assert inventario_page.elemento_interfaz_visible("carrito")
