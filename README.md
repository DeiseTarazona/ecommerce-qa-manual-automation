
# E-commerce QA Manual & Automation

## Descripción del proyecto

Proyecto de portafolio enfocado en el aseguramiento de la calidad de software (QA), utilizando técnicas de pruebas manuales, validación de datos SQL y automatización de pruebas funcionales.

Se utiliza la aplicación web Sauce Demo como entorno de práctica para diseñar, ejecutar y documentar diferentes escenarios de prueba.

## Objetivos

- Diseñar y ejecutar casos de prueba funcionales.
- Identificar y documentar posibles defectos.
- Validar funcionalidades de una tienda virtual.
- Realizar consultas SQL para verificar información.
- Automatizar pruebas utilizando Python, Selenium y pytest.
- Documentar resultados y evidencias de las pruebas.

## Aplicación bajo prueba

**Nombre:** Sauce Demo

**URL:** https://www.saucedemo.com/

**Tipo:** Aplicación web de comercio electrónico.

## Herramientas y tecnologías

| Herramienta | Uso |
|---|---|
| Python | Lenguaje de programación |
| Selenium WebDriver | Automatización web |
| pytest | Ejecución y gestión de pruebas |
| MySQL | Validación de datos SQL |
| Visual Studio Code | Entorno de desarrollo |
| Git y GitHub | Control de versiones y portafolio |
| Google Chrome | Navegador de pruebas |

## Estructura del proyecto

```text
ecommerce-qa-manual-automation/
│
├── README.md
│
├── casos-de-prueba/
│   └── casos_prueba.md
│
├── bugs/
│   └── reporte_bugs.md
│
├── evidencias/
│
└── automatizacion/
    ├── __pycache__/
    ├── conftest.py
    ├── test_login.py
    ├── test_catalogo.py
    ├── test_carrito.py
    ├── test_eliminar_carrito.py
    └── test_ordenar_productos.py
```

## Pruebas manuales

Se diseñaron casos de prueba para validar las siguientes funcionalidades:

- Inicio de sesión.
- Validación de credenciales.
- Visualización del catálogo.
- Agregar productos al carrito.
- Eliminar productos del carrito.
- Ordenamiento de productos.
- Proceso de compra.

Los casos de prueba manuales se encuentran en la carpeta `casos-de-prueba/`.

## Automatización de pruebas

Se desarrollaron pruebas automatizadas utilizando Python, Selenium WebDriver y pytest.

### Casos automatizados

| ID | Caso de prueba | Archivo | Resultado |
|---|---|---|---|
| AT-001 | Inicio de sesión exitoso | test_login.py | PASSED |
| AT-002 | Inicio de sesión con credenciales incorrectas | test_login.py | PASSED |
| AT-003 | Visualización del catálogo | test_catalogo.py | PASSED |
| AT-004 | Agregar producto al carrito | test_carrito.py | PASSED |
| AT-005 | Eliminar producto del carrito | test_eliminar_carrito.py | PASSED |
| AT-006 | Ordenar productos por precio ascendente | test_ordenar_productos.py | PASSED |
| AT-007 | Ordenar productos por nombre A-Z | test_ordenar_productos.py | PASSED |
| AT-008 | Ordenar productos por nombre Z-A | test_ordenar_productos.py | PASSED |
| AT-009 | Ordenar productos por precio descendente | test_ordenar_productos.py | PASSED |

### Configuración de Selenium

Se utiliza `conftest.py` para definir una fixture compartida que permite abrir y cerrar el navegador automáticamente en cada prueba.

### Ejecución de las pruebas

Para ejecutar todas las pruebas automatizadas:

```bash
python -m pytest automatizacion/ -v
```

Para ejecutar un archivo específico:

```bash
python -m pytest automatizacion/test_login.py -v
```

## Resultados de automatización

Última ejecución completa confirmada:

| Indicador | Resultado |
|---|---:|
| Pruebas ejecutadas | 9 |
| Pruebas aprobadas | 9 |
| Pruebas fallidas | 0 |
| Porcentaje de aprobación | 100% |

**Estado:** 9 pruebas automatizadas PASSED.

## Evidencias

Las capturas de pantalla y evidencias de ejecución se almacenan en la carpeta `evidencias/`.

## Proyectos relacionados

- E-commerce QA — Validación de datos con SQL.

## Autora

**Deise Tarazona**

Ingeniera de Sistemas

Área de interés: QA Manual y QA Automation.

Tecnologías en aprendizaje: Python, Selenium, pytest y SQL.
