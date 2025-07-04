from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from allure_pytest.utils import allure_title
import allure
import pytest

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False  # or options.add_argument("--headless=new") to test headless
driver = webdriver.Chrome(options=options)

@allure.title("Negative_Testcase")

def project_negative_testcase():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    username = driver.find_element(By.ID,"login-username")
    password = driver.find_element(By.ID,"login-password")

    username.send_keys("shivani")
    password.send_keys("Pass@123")
    login = driver.find_element(By.ID,"js-login-btn")
    login.click()
    time.sleep(5)

    validation_msg = driver.find_element(By.CLASS_NAME,"notification-box-description")
    assert validation_msg == "Your email, password, IP address or location did not match"

    time.sleep(5)
