# Ecommerce QA – Pruebas Manuales y Automatizadas

## Descripción del proyecto

Proyecto de aseguramiento de calidad (QA) realizado sobre la aplicación web de demostración [Sauce Demo](https://www.saucedemo.com/).

El objetivo es diseñar y ejecutar pruebas manuales y automatizadas para validar las principales funcionalidades de un ecommerce, identificar posibles defectos y verificar el correcto funcionamiento del sistema.

## Objetivos

- Diseñar casos de prueba funcionales.
- Validar el inicio de sesión.
- Verificar el catálogo de productos.
- Comprobar las operaciones del carrito de compras.
- Validar el proceso de checkout.
- Automatizar pruebas funcionales con Selenium y pytest.
- Generar reportes de ejecución de pruebas.

## Tecnologías y herramientas

| Herramienta | Uso |
|---|---|
| Python | Lenguaje de programación |
| Selenium WebDriver | Automatización del navegador |
| pytest | Ejecución y organización de pruebas |
| pytest-html | Generación de reportes HTML |
| Visual Studio Code | Entorno de desarrollo |
| Git y GitHub | Control de versiones |

## Estructura del proyecto

```text
ecommerce-qa-manual-automation/
│
├── automatizacion/
│   ├── conftest.py
│   ├── test_carrito.py
│   ├── test_catalogo.py
│   ├── test_checkout.py
│   ├── test_eliminar_carrito.py
│   ├── test_login.py
│   └── test_ordenar_productos.py
│
├── bugs/
│   └── reporte_bugs.md
│
├── casos-de-prueba/
│   └── casos_prueba.md
│
├── evidencias/
│
├── reportes/
│
├── ejecutar_pruebas.py
├── pytest.ini
├── .gitignore
└── README.md
```

## Pruebas automatizadas

Se implementaron pruebas para validar las siguientes funcionalidades:

| Módulo | Validaciones |
|---|---|
| Login | Inicio de sesión válido e inválido |
| Catálogo | Visualización de productos |
| Carrito | Agregar y eliminar productos |
| Checkout | Acceso y registro de datos del comprador |
| Resumen de compra | Validación de productos, precios, impuestos y total |
| Compra | Finalización de compra y confirmación |
| Ordenamiento | Precio ascendente y descendente, nombre A-Z y Z-A |

## Ejecución de las pruebas

Instalar las dependencias:

```bash
python -m pip install selenium pytest pytest-html
```

Ejecutar todas las pruebas:

```bash
python -m pytest
```

## Reportes de pruebas

Se utiliza `pytest-html` para generar reportes de ejecución en formato HTML.

El reporte principal se guarda en:

```text
reportes/reporte-qa.html
```

Los reportes históricos permiten conservar resultados de ejecuciones anteriores.

## Resultados de ejecución

**Última ejecución registrada: 24/11/2026**

- Pruebas ejecutadas: 14
- Pruebas aprobadas: 14
- Pruebas fallidas: 0

Resultado: 100 % de pruebas aprobadas en esa ejecución.

## Alcance del proyecto

Este proyecto forma parte de mi portafolio de aprendizaje en QA Software Testing, enfocado en pruebas funcionales manuales y automatización de pruebas web.

---

**Repositorio:** Ecommerce QA – Manual Testing & Automation

## Evidencias de ejecución

Se ejecutaron 14 pruebas automatizadas utilizando
Python, Selenium y pytest.

**Resultado de ejecución:**
- Total de pruebas: 14
- Aprobadas: 14
- Fallidas: 0
- Errores: 0

### Reporte de ejecución

![Reporte de ejecución de pruebas](evidencias/evidencia%20reportes/reporte-ejecucion.PNG)

## Cómo ejecutar las pruebas automatizadas

### Requisitos
- Python 3 instalado.
- Google Chrome instalado.

### Instalación de dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar todas las pruebas

```bash
python -m pytest automatizacion/ -v
```

### Generar reporte HTML

```bash
python -m pytest automatizacion/ -v --html=reports/reporte-qa.html --self-contained-html
```

El reporte permite visualizar los resultados de ejecución de los casos automatizados.