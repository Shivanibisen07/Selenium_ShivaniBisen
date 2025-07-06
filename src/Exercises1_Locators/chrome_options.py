from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_chrome_options():

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=900,500")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options) #create a session
    driver.get("https://katalon-demo-cura.herokuapp.com/")  #Navigate to url

    assert True == False


    #Stop python interpreter for 10 sec
    time.sleep(10)