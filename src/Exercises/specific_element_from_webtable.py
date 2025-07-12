from selenium import webdriver
from selenium.webdriver.common.by import By

def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")

    table_rows = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    rows = len(table_rows)
    print("Webtable row count is:" ,rows)

    table_cols = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")
    columns = len(table_cols)
    print("Webtable columns count is:" ,columns)

    first_path = "//table[contains(@id,'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

#created this counter iteration to get all the element's xpath
    for i in range (2, rows+1):
        for j in range (1, columns+1):
            dynamic_path = f"{first_path}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennet is in {country_text}")





