from selenium import webdriver
from selenium.webdriver.common.by import By

def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")

    table = driver.find_element(By.XPATH,"//table[@summary='Sample Table']/tbody")
    rows_table = table.find_elements(By.TAG_NAME,"tr")

    for row in rows_table:
        cols = row.find_elements(By.TAG_NAME,"td")
        for e in cols:
            if "UAE" in e.text:
                 print(e.text)





