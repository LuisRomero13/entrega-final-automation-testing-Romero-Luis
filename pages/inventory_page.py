from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    _PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Verificar que estamos en la página correcta
        self.wait.until(EC.url_contains("/inventory.html"))

    def obtener_titulo(self):
        """Obtiene el título de la página de inventario."""
        return self.driver.find_element(*self._TITLE).text

    def obtener_productos(self):
        """Obtiene la lista de productos disponibles."""
        return self.driver.find_elements(*self._PRODUCTS)

    def obtener_primer_producto(self):
        """Obtiene (nombre, precio) del primer producto del catálogo."""
        producto = self.driver.find_element(*self._PRODUCTS)
        nombre = producto.find_element(*self._PRODUCT_NAME).text
        precio = producto.find_element(*self._PRODUCT_PRICE).text
        return nombre, precio

    def agregar_primer_producto(self):
        """Añade el primer producto disponible al carrito."""
        primer_boton = self.driver.find_elements(*self._ADD_BUTTONS)[0]
        primer_boton.click()
        return self

    def agregar_producto(self, nombre_producto):
        """Añade al carrito el producto cuyo nombre coincide con nombre_producto."""
        slug = nombre_producto.lower().replace(" ", "-")
        boton = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"button[data-test='add-to-cart-{slug}']")
            )
        )
        boton.click()
        return self

    def obtener_contador_carrito(self):
        """Obtiene el número de productos en el carrito."""
        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        except Exception:
            return 0

    def elemento_interfaz_visible(self, elemento: str) -> bool:
        """Comprueba si un elemento clave de la interfaz está visible (menu | filtro | carrito)."""
        locators = {
            "menu": self._MENU_BUTTON,
            "filtro": self._SORT_CONTAINER,
            "carrito": self._CART_LINK,
        }
        return self.driver.find_element(*locators[elemento]).is_displayed()

    def ir_al_carrito(self):
        """Navega a la página del carrito."""
        self.driver.find_element(*self._CART_LINK).click()
        # Importación lazy para evitar dependencias circulares
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def hacer_logout(self):
        """Cierra la sesión del usuario."""
        self.driver.find_element(*self._MENU_BUTTON).click()
        logout_link = self.wait.until(
            EC.element_to_be_clickable(self._LOGOUT_LINK)
        )
        logout_link.click()
        from pages.login_page import LoginPage
        return LoginPage(self.driver)
