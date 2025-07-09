import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

def test_exception():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    try:
        element = driver.find_element(By.ID, "this_id_does_not_exist")
    except NoSuchElementException as nse:
        print(nse.msg)

    time.sleep(4)
