import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture
def setup_driver():
    chrome_options = Options()
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get("https://userinyerface.com/game.html")
    yield driver
    driver.quit()

def test_element1_width(setup_driver):
    element = setup_driver.find_element(By.CLASS_NAME, 'login-form__field-row')
    assert element.value_of_css_property("width") == "372px", "Elementin eni düzgün deyil!"

def test_element1_height(setup_driver):
    element = setup_driver.find_element(By.CLASS_NAME, 'login-form__field-row')
    assert element.value_of_css_property("height") == "40px", "Elementin hündürlüyü düzgün deyil!"

def test_element2_width(setup_driver):
    element = setup_driver.find_element(By.CLASS_NAME, 'align__cell')
    assert element.value_of_css_property("width") == "133.688px", "Elementin eni düzgün deyil!"

def test_font_family(setup_driver):
    element = setup_driver.find_element(By.CLASS_NAME, 'login-form__container')
    assert element.value_of_css_property("font-family") == "sans-serif", "Şrift ailəsi düzgün deyil!"

def test_background_color(setup_driver):
    element = setup_driver.find_element(By.CLASS_NAME, 'login-form__container')
    assert element.value_of_css_property("background") == "#fff", "Fon rəngi düzgün deyil!"
