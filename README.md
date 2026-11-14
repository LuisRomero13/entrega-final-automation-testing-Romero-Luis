# Entrega Proyecto Final - Automatización de Testing
Este proyecto implementa una automatización de pruebas para el sitio SauceDemo, utilizando Selenium WebDriver y Python.

## 🎯 Propósito del Proyecto
El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo:
- Login con credenciales válidas e inválidas
- Verificación del catálogo de productos
- Interacción con el carrito de compras (añadir productos y verificar su contenido)
- Cierre de sesión

## 🛠️ Tecnologías Utilizadas
- **Python:** Lenguaje de programación principal
- **Pytest:** Framework de testing para estructurar y ejecutar pruebas
- **Selenium WebDriver:** Para la automatización de la interfaz web
- **Git/GitHub:** Para control de versiones y compartir el código

## 📁 Estructura del Proyecto
```
proyecto-final-automation-testing-Romero-Luis/
├── conftest.py # Fixture driver() compartida + captura automática de screenshots al fallar
├── pages/ # Page Object Model: una clase por página
│   ├── login_page.py # Encapsula la pantalla de login
│   ├── inventory_page.py # Encapsula la pantalla de inventario
│   ├── cart_page.py # Encapsula la pantalla del carrito
│   └── checkout_page.py # Encapsula el checkout (formulario, resumen y confirmación)
├── datos/ # Datos de prueba externos (data-driven testing)
│   ├── login.csv # Credenciales para el login parametrizado
│   └── productos.json # Productos para el carrito parametrizado
├── tests/ # Casos de prueba (importan pages/, no conocen selectores)
│   ├── test_login_csv.py # Login parametrizado con datos del CSV + smoke
│   ├── test_logout.py # Cierre de sesión (logout)
│   ├── test_catalogo.py # Catálogo de productos y elementos de la interfaz
│   ├── test_carrito_json.py # Carrito parametrizado con productos del JSON + smoke
│   └── test_checkout.py # Flujo completo de compra (checkout)
├── utils/
│   ├── funciones_saucedemo.py # Configuración del WebDriver y capturas
│   └── datos.py # Lectores de CSV/JSON para pytest.mark.parametrize
├── screenshots/ # Capturas; screenshots/fallos/ guarda las capturas de tests fallidos
├── reports/ # el reporte en html y png junto con el log de ejecucion de todos los test
└── extras/ # NO PERTENECE a la entrega pero util para mi aprendizaje con python
```

### 🧩 Page Object Model (POM)
El proyecto aplica el patrón **Page Object Model** (Clase 9): cada página de SauceDemo se representa con una clase que centraliza sus locators y expone métodos de alto nivel. Los tests solo describen flujos de negocio, sin conocer los selectores internos de la interfaz.
## ⚙️ Instalación de Dependencias
1. Asegúrate de tener Python 3.12 o superior instalado.
2. Instala las dependencias necesarias:
pip install selenium pytest pytest-html

3. Descarga el WebDriver correspondiente a tu navegador. En mi caso instalé:
Chromium

4. Asegúrate de que el WebDriver esté en tu PATH o especifica su ubicación en el código.

## ▶️ Ejecución de las Pruebas
**Para ejecutar todas las pruebas:**
.venv/bin/python3 -m pytest -v

**Para generar un reporte HTML:**
.venv/bin/python3 -m pytest -v --html=reports/reporte.html

**Para ejecutar solo los tests de smoke:**
.venv/bin/python3 -m pytest -m smoke -v

## ✅ Funcionalidades Implementadas

1. Automatización de Login (parametrizado con datos/login.csv):
   - Casos de éxito (standard_user, problem_user, performance_glitch_user)
   - Casos de fallo (locked_out_user, credenciales inválidas)

2. Verificación del Catálogo:
   - Comprobación del título de la página
   - Verificación de presencia de productos
   - Verificion de elementos importantes de la interfaz (menu, filtro y carrito)

3. Interacción con el Carrito (parametrizado con datos/productos.json):
   - Añadir cada producto del JSON al carrito
   - Verificar que el contador se incremente
   - Navegar al carrito
   - Comprobar nombre y precio del producto añadido contra el JSON

4. Cierre de Sesión:
   - Verificar que el usuario pueda cerrar sesión correctamente

## ✨ Características Adicionales
- **Capturas automáticas al fallar:** si un test falla, `conftest.py` guarda automáticamente una captura en `screenshots/fallos/` con nombre descriptivo que incluye el nombre del test y la fecha/hora (ej: `FALLO_test_carrito_2026-11-13_10-30-05.png`).

- **Data-driven testing (Clase 10):** los datos de prueba viven en archivos externos (`datos/login.csv` y `datos/productos.json`), leídos por `utils/datos.py` y usados con `@pytest.mark.parametrize`. Agregar un escenario nuevo solo requiere agregar una fila al CSV o un objeto al JSON, sin tocar el código Python.

- **Page Object Model (Clase 9):** clases por página en `pages/` con locators centralizados y métodos de alto nivel.

## 👤 Autor
Luis Romero

## 📝 Notas
Este proyecto fue desarrollado como entrega para el curso de Automatización de Testing.

Todas las pruebas están diseñadas para funcionar con el sitio web SauceDemo en su versión actual.

**IMPORTANTE:** estas lineas de código fueron agregadas solo porque utilizo WSL (no tiene interfaz grafica) y no encontraba mi webDriver:
```
    optiones.add_argument("--headless")
    optiones.add_argument("--disable-dev-shm-usage")
    optiones.binary_location = "/snap/chromium/current/usr/lib/chromium-browser/chrome"
    servicio = Service(executable_path="/usr/bin/chromedriver")
```