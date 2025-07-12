from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_the_awesome_qa_website():
    driver = webdriver.Chrome()  #Chrome session created
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")  #Url has been called

#Fill the form details and submit it

    firstname = driver.find_element(By.ID,"input-firstname")
    firstname.send_keys("Shivani")
    lastname = driver.find_element(By.ID,"input-lastname")
    lastname.send_keys("Bisen")
    email = driver.find_element(By.ID,"input-email")
    email.send_keys("sb12@abc.com")
    telephone = driver.find_element(By.ID,"input-telephone")
    telephone.send_keys("123456")
    password = driver.find_element(By.ID,"input-password")
    password.send_keys("1234!")
    confirm_password = driver.find_element(By.ID, "input-confirm")
    confirm_password.send_keys("1234!")

    driver.find_element(By.XPATH,'//input[@type="checkbox"]').click()

#Here we are submitting the value
    submit = driver.find_element(By.XPATH,'//input[@type="submit"]')
    submit.click()
    time.sleep(5)

    source_page = driver.page_source
    assert "Your Account Has Been Created!" in source_page
    time.sleep(2)
    driver.quit()


