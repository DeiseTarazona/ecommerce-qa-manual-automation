
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_eliminar_producto_carrito(driver):
    driver.get("https://www.saucedemo.com/")

    # Iniciar sesión
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Esperar que aparezca el botón de agregar
    boton_agregar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )

    # Agregar mochila
    boton_agregar.click()

    # Esperar que aparezca el carrito
    carrito = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    )

    # Entrar al carrito
    carrito.click()

    # Esperar que aparezca el botón eliminar
    boton_eliminar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "remove-sauce-labs-backpack")
        )
    )

    # Eliminar mochila
    boton_eliminar.click()

    # Esperar que desaparezca el contador
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    # Comprobar que el carrito esté vacío
    productos = driver.find_elements(
        By.CLASS_NAME, "cart_item"
    )

    assert len(productos) == 0
