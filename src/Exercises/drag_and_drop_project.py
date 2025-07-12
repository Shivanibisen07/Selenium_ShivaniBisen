import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def verify_action_class():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    element_to_drag = driver.find_element(By.ID,"draggable")
    element_where_to_drop = driver.find_element(By.ID,"droppable")

    action = ActionChains(driver)
    action.drag_and_drop(element_to_drag, element_where_to_drop).perform()

    time.sleep(5)
    driver.quit()
verify_action_class()