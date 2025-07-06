import time

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def ebay_website_mini_project():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers")
    time.sleep(5)
#Search for the mac mini and click on send button
    search_item = driver.find_element(By.XPATH, "//input[@title='Search']")
    search_item.send_keys('mac mini')
    search_button = driver.find_element(By.XPATH, "//button[@class='gh-search-button btn btn--primary']")
    search_button.click()

    time.sleep(5)
    print("Current Url:",driver.current_url)
ebay_website_mini_project()


#Get all the titles and Get all the prices\
    item_title = driver.find_elements(By.XPATH,"//span[@role='heading']")
    item_price = driver.find_elements(By.XPATH,"//span[@class='s-item__price']")
    print(item_title and item_price)
ebay_website_mini_project()


