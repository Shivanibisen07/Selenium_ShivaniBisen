from selenium import webdriver
import time
from selenium.webdriver.common.by import By




def ebay_website_mini_project():

    driver = webdriver.Chrome()

    try:
        driver.maximize_window()
        driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers")
        time.sleep(3)
    #Search for the mac mini and click on send button
        search_item = driver.find_element(By.XPATH, "//input[@aria-label='Search for anything']")
        search_item.send_keys('mac mini')
        search_button = driver.find_element(By.XPATH, "//button[@class='gh-search-button btn btn--primary']")
        search_button.click()
        time.sleep(5)
        print("Current Url:",driver.current_url)



    #Get all the titles and Get all the prices\
        titles = driver.find_elements(By.XPATH,"//div[@class='s-item__title']")
        print(len(titles))
        prices = driver.find_elements(By.XPATH,"//div[@class='s-item__detail s-item__detail--primary']")
        print(len(prices))

        if len(titles) != len(prices):
            print("Mismatch in the number of titles and prices.")
        else:

            product_data = []
            price_values = []

            for title, price in zip(titles, prices):
                title_text = title.text
                price_text = price.text.replace(",", "").replace("$", "").split()[0]

                try:
                    price_value = float(price_text)
                    product_data.append((title_text, price_value))
                    price_values.append(price_value)
                except ValueError:
                    print(f"Skipping invalid price: {price_text}")

            print("\nProduct Titles and Prices:")
            for title, price in product_data:
                print(f"{title} - ${price}")

            if price_values:
                max_price = max(price_values)
                min_price = min(price_values)
                print(f"\nMaximum Price: ${max_price}")
                print(f"Minimum Price: ${min_price}")
            else:
                print("\nNo valid prices found.")
    finally:
        driver.quit()
ebay_website_mini_project()







