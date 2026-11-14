# 1: Funcionalidades Específicas:

## 1. Pruebas de UI (Selenium WebDriver):

Automatización de Casos de Prueba:
- Implementa al menos 5 casos de prueba para un sitio web demo (puede ser saucedemo.com, automationpractice.com, o cualquier otro sitio de práctica)
- Los casos de prueba deben cubrir flujos completos (ejemplo: login, navegación, búsqueda, añadir producto al carrito, checkout)
- Incluye al menos un escenario negativo (ejemplo: login con credenciales inválidas)

Manejo de Datos de Prueba:
- Implementa alguna forma de parametrización para ejecutar las pruebas con diferentes conjuntos de datos
- Utiliza fuentes externas (archivos CSV, JSON, etc.) para leer los datos de prueba

Manejo de Datos de Prueba:
- Implementa alguna forma de parametrización para ejecutar las pruebas con diferentes conjuntos de datos
- Utiliza fuentes externas (archivos CSV, JSON, etc.) para leer los datos de prueba

Implementación de Page Object Model:
- Crea clases para cada página que vayas a automatizar
- Implementa métodos que representen acciones en cada página
- Separa la lógica de las pruebas de la lógica de interacción con la página

Gestión de Capturas de Pantalla:
- Implementa una funcionalidad que capture screenshots automáticamente cuando una prueba falla
- Almacena las capturas con nombres descriptivos que incluyan fecha/hora y nombre del test

## 2. Pruebas de API (Requests):

Automatización de Endpoints:
- Implementa al menos 3 casos de prueba para una API pública (puede ser ReqRes, JSONPlaceholder, o cualquier otra API pública)
- Cubre diferentes métodos HTTP (GET, POST, DELETE)

Validación de Respuestas:
- Verifica códigos de estado HTTP
- Valida estructura y contenido de las respuestas JSON
- Implementa assertions para diferentes escenarios (éxito, error, etc.)

Encadenamiento de Peticiones (Opcional):
- Implementa un flujo donde una petición dependa del resultado de otra (ejemplo: crear un recurso y luego obtenerlo)

## 3. Generación de Reportes:

Reportes HTML:
- Configura pytest para generar reportes HTML detallados
- Los reportes deben mostrar claramente los tests ejecutados, su estado (pasado/fallado) y duración
- Incluye capturas de pantalla en los reportes para las pruebas fallidas

Logging:
- Implementa un sistema de logging que registre pasos clave durante la ejecución
- El log debe ser lo suficientemente detallado para facilitar la depuración

## 4. Integración con CI/CD:

Github Actions
- Configura GitHub Actions para ejecutar tus pruebas automatizadas cuando se realice un push al repositorio
- Genera y almacena los reportes como artefactos de la ejecución

## 5. Control de Versiones y Documentación:

Repositorio en GitHub:
- Sube el proyecto a un repositorio en GitHub
- Mantén un historial de commits que documente el progreso del proyecto
- Usa ramas para desarrollar funcionalidades y luego fusiónalas con la rama principal

README.md:
Incluye un archivo README.md que explique:
- El propósito del proyecto
- Las tecnologías utilizadas
- La estructura del proyecto
- ¿Cómo instalar las dependencias?
- ¿Cómo ejecutar las pruebas?
- ¿Cómo interpretar los reportes generados?