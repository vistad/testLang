# reads the language param from the CLI and starts the browser with the defined language.
# pytest --language=es test_items.py
# pytest --language=fr test_items.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose lang")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    print("\nquit browser...")
    yield browser
    browser.quit()



