
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


def test_eliminar_producto_carrito(driver):

    driver.get("https://www.saucedemo.com/")

    espera = WebDriverWait(driver, 10)

    # Iniciar sesión
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Esperar catálogo
    espera.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    # Agregar mochila
    espera.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    # Entrar al carrito
    espera.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    ).click()

    # Esperar que cargue el carrito
    espera.until(EC.url_contains("cart.html"))

    # Buscar nuevamente el botón eliminar si el DOM se actualiza
    def boton_eliminar_disponible(driver):
        try:
            boton = driver.find_element(
                By.ID, "remove-sauce-labs-backpack"
            )

            if boton.is_displayed() and boton.is_enabled():
                return boton

            return False

        except StaleElementReferenceException:
            return False

    boton_eliminar = espera.until(boton_eliminar_disponible)

    # Eliminar producto
    boton_eliminar.click()

    # Verificar que el carrito quede vacío
    espera.until(
        lambda driver: len(
            driver.find_elements(By.CLASS_NAME, "cart_item")
        ) == 0
    )

    assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0
