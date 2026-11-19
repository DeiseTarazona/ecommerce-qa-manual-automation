
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_mostrar_productos(driver):
    driver.get("https://www.saucedemo.com/")

    # Iniciar sesión
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Esperar que aparezca el catálogo
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    # Obtener los productos
    productos = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    # Verificar que existan 6 productos
    assert len(productos) == 6

    # Verificar que el nombre del producto sea visible
    nombre = driver.find_element(
        By.CLASS_NAME, "inventory_item_name"
    )

    assert nombre.is_displayed()
