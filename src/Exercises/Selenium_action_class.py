import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def verify_action_class():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    first_name = driver.find_element(By.XPATH,"//input[@name='firstname']")

    action = ActionChains(driver=driver)
    (action.key_down(Keys.SHIFT)
     .send_keys_to_element(first_name,"the testing academy")
     .key_up(Keys.SHIFT)
     .perform())

    time.sleep(10)
    driver.quit()
verify_action_class()



