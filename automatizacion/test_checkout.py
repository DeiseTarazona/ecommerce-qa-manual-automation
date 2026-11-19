
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.saucedemo.com/"


# ==========================================
# FUNCIONES AUXILIARES
# ==========================================

def iniciar_sesion(driver):
    driver.get(URL)

    driver.find_element(
        By.ID, "user-name"
    ).send_keys("standard_user")

    driver.find_element(
        By.ID, "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID, "login-button"
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )


def agregar_mochila_y_abrir_carrito(driver):
    boton_agregar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    boton_agregar.click()

    carrito = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    )
    carrito.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )


def abrir_checkout(driver):
    boton_checkout = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "checkout")
        )
    )
    boton_checkout.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "first-name")
        )
    )


def completar_datos_comprador(driver):
    driver.find_element(
        By.ID, "first-name"
    ).send_keys("Deise")

    driver.find_element(
        By.ID, "last-name"
    ).send_keys("Tarazona")

    driver.find_element(
        By.ID, "postal-code"
    ).send_keys("12001")


def continuar_al_resumen(driver):
    boton_continue = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "continue")
        )
    )
    boton_continue.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_info")
        )
    )


# ==========================================
# AT-010: ACCEDER AL CHECKOUT
# ==========================================

def test_acceder_checkout(driver):
    iniciar_sesion(driver)

    agregar_mochila_y_abrir_carrito(driver)

    abrir_checkout(driver)

    assert "checkout-step-one.html" in driver.current_url


# ==========================================
# AT-011: COMPLETAR DATOS DEL COMPRADOR
# ==========================================

def test_completar_datos_comprador(driver):
    iniciar_sesion(driver)

    agregar_mochila_y_abrir_carrito(driver)

    abrir_checkout(driver)

    completar_datos_comprador(driver)

    continuar_al_resumen(driver)

    assert "checkout-step-two.html" in driver.current_url


# ==========================================
# AT-012: VALIDAR RESUMEN DE COMPRA
# ==========================================

def test_validar_resumen_compra(driver):
    iniciar_sesion(driver)

    agregar_mochila_y_abrir_carrito(driver)

    abrir_checkout(driver)

    completar_datos_comprador(driver)

    continuar_al_resumen(driver)

    # Validar nombre del producto
    producto = driver.find_element(
        By.CLASS_NAME, "inventory_item_name"
    )
    assert producto.text == "Sauce Labs Backpack"

    # Validar precio
    precio = driver.find_element(
        By.CLASS_NAME, "inventory_item_price"
    )
    assert precio.text == "$29.99"

    # Validar subtotal
    subtotal = driver.find_element(
        By.CLASS_NAME, "summary_subtotal_label"
    )
    assert subtotal.text == "Item total: $29.99"

    # Validar impuestos
    impuestos = driver.find_element(
        By.CLASS_NAME, "summary_tax_label"
    )
    assert impuestos.text == "Tax: $2.40"

    # Validar total
    total = driver.find_element(
        By.CLASS_NAME, "summary_total_label"
    )
    assert total.text == "Total: $32.39"


# ==========================================
# AT-013: FINALIZAR COMPRA
# ==========================================

def test_finalizar_compra(driver):
    iniciar_sesion(driver)

    agregar_mochila_y_abrir_carrito(driver)

    abrir_checkout(driver)

    completar_datos_comprador(driver)

    continuar_al_resumen(driver)

    # Finalizar compra una sola vez
    boton_finish = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "finish")
        )
    )
    boton_finish.click()

    # Verificar confirmación
    mensaje = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    )

    assert mensaje.text == "Thank you for your order!"


# ==========================================
# AT-014: VALIDAR CARRITO DESPUÉS DE COMPRAR
# ==========================================

def test_carrito_vacio_despues_compra(driver):
    iniciar_sesion(driver)

    agregar_mochila_y_abrir_carrito(driver)

    abrir_checkout(driver)

    completar_datos_comprador(driver)

    continuar_al_resumen(driver)

    # Finalizar compra
    driver.find_element(By.ID, "finish").click()

    # Esperar confirmación
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    )

    # Volver al catálogo
    driver.find_element(By.ID, "back-to-products").click()

    # Verificar que el carrito esté vacío
    indicadores = driver.find_elements(
    By.CLASS_NAME, "shopping_cart_badge"
    )

    assert len(indicadores) == 0
