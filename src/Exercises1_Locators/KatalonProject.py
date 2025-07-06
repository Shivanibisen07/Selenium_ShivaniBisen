'''1. Try the Selenium IDE, Record the One Test
open this → https://katalon-demo-cura.herokuapp.com/
Click on the button Make appointment
on the Next Page → Enter the username, password and submit button
Export the script to Python.'''
import time

from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By

@allure.title("Verify the Katalon app flow")

def test_click_button_on_katalon():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_button = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_button.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(2)
    username = driver.find_element(By.ID,"txt-username")
    password = driver.find_element(By.ID,"txt-password")
    username.send_keys("Shivani")
    password.send_keys("123")
    login = driver.find_element(By.ID,"btn-login")
    login.click()

    time.sleep(5)
    driver.quit()


