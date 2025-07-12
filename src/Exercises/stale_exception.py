import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

def stale_exception():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    try:
        text_area = driver.find_element(By.NAME,"q")
        driver.refresh()

        text_area.send_keys("Shivani")
    except StaleElementReferenceException as see:
        print(see)
        print("Stale element reference")

    time.sleep(5)
stale_exception()