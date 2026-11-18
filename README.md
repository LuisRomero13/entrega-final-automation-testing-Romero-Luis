# Proyecto Final - Automatización de Testing

Framework de automatización de pruebas para **SauceDemo** (UI) y para las APIs públicas **reqres.in** y **JSONPlaceholder**. Incluye Page Object Model, datos de prueba externos, validación de respuestas, reportes HTML con capturas automáticas y logging centralizado.

## Propósito

El proyecto demuestra un flujo completo de testing automatizado:

- Pruebas de UI con Selenium WebDriver sobre flujos de login, catálogo, carrito, checkout y logout.
- Pruebas de API con Requests sobre operaciones GET, POST, PUT, PATCH y DELETE.
- Casos positivos y negativos, incluyendo login con credenciales inválidas y endpoints inexistentes.
- Parametrización de pruebas mediante archivos CSV y JSON.
- Evidencia de ejecución mediante reportes HTML, capturas de fallos y logs.

## Tecnologías utilizadas

- Python 3.12
- Pytest 9
- Selenium WebDriver 4
- Requests
- pytest-html (reportes HTML autocontenidos)
- pytest-metadata (información del entorno en el reporte)
- CSV y JSON como fuentes de datos de prueba
- Chrome/Chromium en modo headless

## Estructura del proyecto

```
.
├── conftest.py              # Fixtures de UI, logging, capturas y hooks del reporte
├── pytest.ini               # Configuración de Pytest, reporte HTML y markers
├── pages/                   # Page Object Model
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                   # Pruebas de UI
│   ├── test_login_csv.py
│   ├── test_catalogo.py
│   ├── test_carrito_json.py
│   ├── test_checkout.py
│   └── test_logout.py
├── test_api/                # Pruebas de API
│   ├── conftest.py
│   ├── test_login_api.py
│   ├── test_users_api.py
│   ├── test_create_user_api.py
│   ├── test_posts_api.py
│   └── test_post_lifecycle.py
├── datos/                   # Datos de prueba externos
│   ├── login.csv
│   └── productos.json
├── utils/                   # Utilidades del framework
│   ├── datos.py             # Lectura de CSV y JSON
│   ├── funciones_saucedemo.py  # Configuración de Chrome y capturas
│   └── logger.py            # Logger centralizado con rotación
├── reports/                 # Reporte HTML y capturas generadas
│   └── screens/
├── logs/                    # Logs de ejecución
│   └── suite.log
└── extras/                  # Prácticas y material auxiliar, no forma parte de la entrega
```

La suite contiene **26 pruebas**: 14 de UI y 12 de API.

## Requisitos previos

- Python 3.12 o superior.
- Chrome o Chromium instalado.
- ChromeDriver compatible con la versión del navegador.

Las rutas del binario de Chromium y de ChromeDriver se configuran en `utils/funciones_saucedemo.py`. Si se ejecuta en otro entorno, ajustar `binary_location` y `executable_path` según corresponda.

## Instalación de dependencias

```bash
python -m venv .venv
source .venv/bin/activate
pip install selenium pytest pytest-html requests
```

En Windows, la activación del entorno virtual es:

```bash
.venv\Scripts\activate
```

## Ejecución de las pruebas

```bash
# Suite completa: UI + API
pytest

# Solo pruebas de UI
pytest tests/

# Solo pruebas de API
pytest test_api/ -m api

# Por marker
pytest -m smoke
pytest -m e2e

# Un archivo o un test específico
pytest tests/test_login_csv.py
pytest -k "login"
```

Al finalizar, Pytest genera automáticamente `reports/reporte.html` y escribe el log de la ejecución en `logs/suite.log`.

## Cómo interpretar los reportes generados

### Reporte HTML

Abrir `reports/reporte.html` en el navegador. El reporte incluye:

- **Resumen general:** cantidad de tests pasados, fallados, omitidos y duración total.
- **Tabla de resultados:** columnas `Result`, `Test`, `URL`, `Duration` y `Links`.
  - `Result`: estado del test (`Passed`, `Failed`, etc.).
  - `Test`: nombre y ruta del test ejecutado.
  - `URL`: última página visitada por los tests de UI (los tests de API muestran `-`).
  - `Duration`: tiempo de ejecución de cada test.
  - `Links`: adjuntos del test.
- **Detalle del fallo:** al expandir un test fallido se muestra el mensaje de error, el traceback, el log capturado y la captura de pantalla adjunta.
- **Entorno:** versión de Python, plataforma y plugins utilizados.

### Capturas de pantalla

- Cuando un test de UI falla, se guarda una imagen en `reports/screens/` con el nombre del test.
- La imagen se incrusta automáticamente en el reporte HTML, por lo que el reporte autocontenido puede compartirse sin archivos adicionales.

### Logs

`logs/suite.log` registra los pasos clave de la ejecución. Cada línea tiene el formato:

```
2026-11-18 14:50:56 INFO talentolab - Ingresando usuario: standard_user
2026-11-18 14:50:56 INFO talentolab - Enviando formulario de login
2026-11-18 14:50:56 INFO talentolab - FIN test: tests/test_login_csv.py::test_login_usuario_valido_smoke -> passed (0.83s)
```

- `INFO`: inicio y fin de tests, acciones sobre páginas, requests y validaciones.
- `ERROR`: tests fallidos y errores al guardar capturas.
- El archivo rota automáticamente al alcanzar 1 MB y conserva hasta 5 respaldos.

Para generar un reporte separado de solo API:

```bash
pytest test_api/ -m api -o addopts="-v --html=reports/reporte_api.html --self-contained-html"
```

Los reportes y logs se regeneran en cada ejecución; las capturas y los archivos de log están excluidos del control de versiones.

## Control de versiones

- La rama `main` contiene la versión estable del proyecto.
- Las funcionalidades se desarrollaron en ramas `feat/...` y se integraron mediante Pull Requests.
- El historial de commits documenta la evolución del framework: Page Object Model, pruebas de API, reportes, capturas, logging y documentación.

## Autor

Luis Romero

Este proyecto fue desarrollado como entrega final para el curso de Automatización de Testing.
