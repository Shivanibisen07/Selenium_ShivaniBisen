import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select

def test_radio_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    female_radio_btn = driver.find_element(By.XPATH,"//input[@id='sex-1']")
    female_radio_btn.click()

    years_of_experience = driver.find_element(By.XPATH,"//input[@id='exp-2']")
    years_of_experience.click()


    profession = driver.find_element(By.XPATH,"//input[@id='profession-1']")
    profession.click()

    time.sleep(5)



