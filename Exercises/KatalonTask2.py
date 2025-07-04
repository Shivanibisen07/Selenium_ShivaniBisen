'''Create a Selenium Script to verify the title for
Open the Page - https://katalon-demo-cura.herokuapp.com/
Verify the current URL, current title
In the page source add a assertion that “CURA Healthcare Service” exist in the page. driver.pageSource() - String'''

from selenium import webdriver
import pytest
import allure

@allure.title("Verify the title of page")

def test_verify_the_title_of_page():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    page_title = driver.title
    print(page_title)
    page_source = driver.page_source
    assert "CURA Healthcare Service" in page_source
    print("page_source")
    driver.quit()


