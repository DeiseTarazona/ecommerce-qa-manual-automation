
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_agregar_producto_carrito(driver):
    driver.get("https://www.saucedemo.com/")

    # Iniciar sesión
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Esperar que aparezca el botón de agregar
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )

    # Agregar mochila al carrito
    boton.click()

    # Esperar que aparezca el contador
    contador = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    # Verificar que exista un producto
    assert contador.text == "1"
