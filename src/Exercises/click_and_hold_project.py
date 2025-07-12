import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def verify_action_class():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    element_to_hold = driver.find_element(By.ID,"draggable")

    action = ActionChains(driver)
    action.click_and_hold(on_element=element_to_hold).perform()

    time.sleep(5)
    driver.quit()
verify_action_class()