# pytest -v -s ~/seleniumPy/testLanguage/test_items.py
# pytest -v -s --language=es ~/seleniumPy/testLanguage/test_items.py

from selenium.webdriver.common.by import By
import time

expected_value = "Añadir al carrito"

def test_button_present(browser):
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").is_displayed(), \
    "The button Add to cart is missing"
    actual_value = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").text
    assert(expected_value == actual_value), \    # extra assert to check if the language is not Spanish
    "The language is not Spanish"
