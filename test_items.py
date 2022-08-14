# pytest -v -s --language=es test_items.py
# Expected value: Añadir al carrito
# pytest -v -s --language=fr test_items.py
# Expected value: Ajouter au panier

from selenium.webdriver.common.by import By
import time

def test_button_present(browser):
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").is_displayed(), \
    "The button Add to cart is missing"

