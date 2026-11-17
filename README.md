# Proyecto Final - Automatización de Testing

Automatización de pruebas de UI sobre **SauceDemo** y de API sobre **reqres.in** y **JSONPlaceholder**, usando Python, Pytest, Selenium y Requests.

## Tecnologías utilizadas

- Python 3.12
- Pytest + pytest-html
- Selenium WebDriver
- Requests

## Estructura

```
.
├── conftest.py              # Fixtures de UI y captura automática de fallos
├── pytest.ini               # Reporte HTML y markers
├── pages/                   # Page Object Model: login, inventario, carrito y checkout
├── tests/                   # Tests de UI
├── test_api/                # Tests de API
│   ├── conftest.py          # Fixtures de URLs y recurso creado
│   ├── test_login_api.py
│   ├── test_users_api.py
│   ├── test_create_user_api.py
│   ├── test_posts_api.py
│   └── test_post_lifecycle.py
├── datos/                   # login.csv y productos.json
├── utils/                   # Configuración de Chrome, capturas y lectura de datos
├── reports/                 # Reportes HTML generados
├── screenshots/fallos/      # Capturas de tests UI fallidos
└── extras/                  # Prácticas, no forma parte de la entrega
```

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install selenium pytest pytest-html requests
```

Se requiere Chrome/Chromium y ChromeDriver. La ruta se configura en `utils/funciones_saucedemo.py`.

## Ejecución de las pruebas

```bash
# Todo: UI + API
pytest

# Solo UI
pytest tests/

# Solo API
pytest test_api/ -m api

# Markers
pytest -m smoke
pytest -m e2e
```

## Reportes

- `pytest.ini` genera automáticamente `reports/reporte.html`.
- Los tests de UI fallidos guardan una captura en `screenshots/fallos/` con nombre, fecha y hora.
- Para un reporte de solo API:

```bash
pytest test_api/ -m api -o addopts="-v --html=reports/reporte_api.html --self-contained-html"
```

## Autor

Luis Romero

## 📝 Notas
Este proyecto fue desarrollado como entrega para el curso de Automatización de Testing.

Utilizo por proyecto en mi caso: .venv/bin/python3 -m pytest test_api/ -m api