import time

from pycparser.ply.yacc import resultlimit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_alert_normal():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")


    js_alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    js_alert.click()

    WebDriverWait(driver=driver,timeout=10).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    result = driver.find_element(By.ID,"result").text
    assert result == "You successfully clicked an alert"

    time.sleep(5)


def test_alert_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")


    js_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    js_confirm.click()

    WebDriverWait(driver=driver,timeout=10).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.dismiss()

    result = driver.find_element(By.ID,"result").text
    assert result == "You clicked: Cancel"

    time.sleep(5)

def test_alert_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    js_prompt = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    js_prompt.click()

    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("Shivani")

    alert.accept()

    result = driver.find_element(By.ID, "result").text
    assert result == "You entered: Shivani"

    time.sleep(5)

