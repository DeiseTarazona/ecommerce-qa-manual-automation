
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait



def iniciar_sesion(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Esperar hasta que aparezca la lista de ordenamiento
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "product_sort_container")
        )
    )



def obtener_precios(driver):
    elementos = driver.find_elements(
        By.CLASS_NAME, "inventory_item_price"
    )

    return [
        float(elemento.text.replace("$", ""))
        for elemento in elementos
    ]


def obtener_nombres(driver):
    elementos = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )

    return [elemento.text for elemento in elementos]


def test_ordenar_precio_ascendente(driver):
    iniciar_sesion(driver)

    lista = driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    )
    Select(lista).select_by_value("lohi")

    WebDriverWait(driver, 10).until(
        lambda d: obtener_precios(d) == sorted(obtener_precios(d))
    )

    precios = obtener_precios(driver)

    assert precios == sorted(precios)


def test_ordenar_nombre_alfabetico(driver):
    iniciar_sesion(driver)

    lista = driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    )
    Select(lista).select_by_value("az")

    WebDriverWait(driver, 10).until(
        lambda d: obtener_nombres(d) == sorted(obtener_nombres(d))
    )

    nombres = obtener_nombres(driver)

    assert nombres == sorted(nombres)


def test_ordenar_nombre_alfabetico_inverso(driver):
    iniciar_sesion(driver)

    lista = driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    )
    Select(lista).select_by_value("za")

    WebDriverWait(driver, 10).until(
        lambda d: obtener_nombres(d) == sorted(
            obtener_nombres(d), reverse=True
        )
    )

    nombres = obtener_nombres(driver)

    assert nombres == sorted(nombres, reverse=True)


def test_ordenar_precio_descendente(driver):
    iniciar_sesion(driver)

    lista = driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    )
    Select(lista).select_by_value("hilo")

    WebDriverWait(driver, 10).until(
        lambda d: obtener_precios(d) == sorted(
            obtener_precios(d), reverse=True
        )
    )

    precios = obtener_precios(driver)

    assert precios == sorted(precios, reverse=True)
