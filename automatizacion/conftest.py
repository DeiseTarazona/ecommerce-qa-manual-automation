
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    navegador = webdriver.Chrome()
    yield navegador
    navegador.quit()
1