import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-gb", help="Language")
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    #browser_name = None
    user_language = request.config.getoption("language")
    option = Options()
    option.add_experimental_option('prefs', {'init.accept_language': user_language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    #return user_language