import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

def test_window_handle():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")

    #parent_window = driver.current_window_handle

    link = driver.find_element(By.LINK_TEXT,"Click Here")
    link.click()

    window_handles = driver.window_handles
    print(window_handles)

    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("Testcase Passed")
            break


    time.sleep(5)
    driver.quit()


