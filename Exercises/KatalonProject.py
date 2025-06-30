from selenium import webdriver
import pytest
import allure

@allure.title("Verify the Katalon app flow")

def test_click_button_on_katalon():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.find_element(BY.ID,"btn-make-appointment").click()


