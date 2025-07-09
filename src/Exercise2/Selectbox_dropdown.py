import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_select_box_dropdown():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    select_html_tag = driver.find_element(By.ID,"dropdown")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "dropdown")))

    dropdown = Select(select_html_tag)  #Will give all the select option

    dropdown.select_by_visible_text("Option 2")

    time.sleep(5)





