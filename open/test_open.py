from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

import time

options = ChromeOptions()
service = ChromeService(executable_path=ChromeDriverManager().install())

with webdriver.Chrome(service=service, options=options) as browser:
    browser.get("https://stepik.org/course/575/syllabus")
    time.sleep(9)