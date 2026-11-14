import pytest

from utils.datos import leer_json_productos

PRODUCTOS = leer_json_productos()


# Test que agrega cada producto del JSON al carrito
@pytest.mark.parametrize("producto", PRODUCTOS, ids=lambda producto: producto["nombre"])
def test_agregar_producto_desde_json(usuario_logueado, producto):
    print(f"Agregando producto: {producto['nombre']}")

    usuario_logueado.agregar_producto(producto["nombre"])

    # Verificar que el carrito tenga 1 artículo
    assert usuario_logueado.obtener_contador_carrito() == 1

    # Navegar al carrito y verificar que el producto esté presente
    cart_page = usuario_logueado.ir_al_carrito()
    assert cart_page.obtener_nombres_productos() == [producto["nombre"]]

    # Verificar que el precio mostrado coincida con el del JSON
    precio_mostrado = float(cart_page.obtener_precios_productos()[0].replace("$", ""))
    assert precio_mostrado == producto["precio"]
    print(f"Precio verificado: {precio_mostrado}")


# Test de smoke que verifica funcionalidad básica del carrito
@pytest.mark.smoke
def test_carrito_smoke(usuario_logueado):
    usuario_logueado.agregar_primer_producto()
    assert usuario_logueado.obtener_contador_carrito() == 1
