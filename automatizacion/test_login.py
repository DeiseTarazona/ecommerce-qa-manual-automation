
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize(
    "usuario, contrasena, acceso_esperado",
    [
        ("standard_user", "secret_sauce", True),
        ("usuario_incorrecto", "clave_incorrecta", False),
    ],
)
def test_inicio_sesion(driver, usuario, contrasena, acceso_esperado):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(contrasena)
    driver.find_element(By.ID, "login-button").click()

    if acceso_esperado:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_list")
            )
        )
        assert "inventory" in driver.current_url
    else:
        mensaje = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )
        assert "Username and password do not match" in mensaje.text
