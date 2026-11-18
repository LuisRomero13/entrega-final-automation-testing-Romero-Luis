from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.logger import logger

NOMBRE = "Luis"
APELLIDO = "Romero"
CODIGO_POSTAL = "5000"


# Verifica el flujo completo de compra: agregar producto, checkout y confirmación
def test_checkout_completo(usuario_logueado):
    logger.info("Iniciando flujo completo de checkout")
    # Agregar producto al carrito y navegar al checkout
    usuario_logueado.agregar_primer_producto()
    cart_page = usuario_logueado.ir_al_carrito()
    assert isinstance(cart_page, CartPage)

    checkout_page = cart_page.proceder_checkout()
    assert isinstance(checkout_page, CheckoutPage)

    # Completar el formulario de datos personales y avanzar al resumen
    resumen = checkout_page.completar_formulario(NOMBRE, APELLIDO, CODIGO_POSTAL).continuar()

    # Verificar que el producto esté en el resumen
    nombres = resumen.obtener_nombres_productos()
    assert "Sauce Labs Backpack" in nombres
    logger.info("Productos en el resumen de la orden: %s", nombres)

    # Finalizar la compra y verificar el mensaje de confirmación
    completa = resumen.finalizar_compra()
    mensaje = completa.obtener_mensaje()
    assert mensaje == "Thank you for your order!"
    logger.info("Compra confirmada: %s", mensaje)
