from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # Paso 1: formulario de datos personales (checkout-step-one.html)
    _FIRST_NAME = (By.ID, "first-name")
    _LAST_NAME = (By.ID, "last-name")
    _POSTAL_CODE = (By.ID, "postal-code")
    _CONTINUE_BUTTON = (By.ID, "continue")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Verificar que estamos en la página correcta
        self.wait.until(EC.url_contains("checkout-step-one.html"))

    def completar_formulario(self, nombre, apellido, codigo_postal):
        """Completa el formulario de datos personales."""
        campo_nombre = self.wait.until(
            EC.visibility_of_element_located(self._FIRST_NAME)
        )
        campo_nombre.send_keys(nombre)
        self.driver.find_element(*self._LAST_NAME).send_keys(apellido)
        self.driver.find_element(*self._POSTAL_CODE).send_keys(codigo_postal)
        return self

    def continuar(self):
        """Avanza al resumen de la orden (paso 2)."""
        self.driver.find_element(*self._CONTINUE_BUTTON).click()
        return CheckoutResumenPage(self.driver)

    def esta_error_visible(self) -> bool:
        """Comprueba si aparece un mensaje de error al omitir campos."""
        try:
            self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
            return True
        except Exception:
            return False


class CheckoutResumenPage:
    # Paso 2: resumen de la orden (checkout-step-two.html)
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    _FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Verificar que estamos en la página correcta
        self.wait.until(EC.url_contains("checkout-step-two.html"))

    def obtener_nombres_productos(self):
        """Obtiene los nombres de los productos en el resumen."""
        elementos = self.driver.find_elements(*self._ITEM_NAMES)
        return [elemento.text for elemento in elementos]

    def obtener_precios_productos(self):
        """Obtiene los precios de los productos en el resumen."""
        elementos = self.driver.find_elements(*self._ITEM_PRICES)
        return [elemento.text for elemento in elementos]

    def finalizar_compra(self):
        """Finaliza la compra y navega a la página de confirmación."""
        self.driver.find_element(*self._FINISH_BUTTON).click()
        return CheckoutCompletaPage(self.driver)


class CheckoutCompletaPage:
    # Paso 3: confirmación del pedido (checkout-complete.html)
    _MENSAJE_COMPLETO = (By.CSS_SELECTOR, "h2[data-test='complete-header']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Verificar que estamos en la página correcta
        self.wait.until(EC.url_contains("checkout-complete.html"))

    def obtener_mensaje(self):
        """Obtiene el mensaje de confirmación del pedido."""
        return self.driver.find_element(*self._MENSAJE_COMPLETO).text
