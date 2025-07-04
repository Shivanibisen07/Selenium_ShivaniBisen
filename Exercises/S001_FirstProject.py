from selenium import webdriver
import allure
import pytest


@allure.title("Verify the title of webpage app.vwo.com")

def test_open_vwo_login():
    driver = webdriver.Chrome()  # Create a session
    driver.get("https://app.vwo.com") # For navigating to the url
    driver.maximize_window()
    print(driver.title)
    print(driver.current_url)


