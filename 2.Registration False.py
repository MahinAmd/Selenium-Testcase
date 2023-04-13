from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/accounts/register/")
driver.maximize_window()


driver.find_element(By.XPATH, '//*[@id="id_first_name"]').send_keys("")
driver.find_element(By.XPATH, '//*[@id="id_last_name"]').send_keys("Mahin")
driver.find_element(By.XPATH, '//*[@id="id_email"]').send_keys("")
driver.find_element(By.XPATH, '//*[@id="id_account_type"]').send_keys("Salary")
driver.find_element(By.XPATH, '//*[@id="id_gender"]').send_keys("Male")
driver.find_element(By.XPATH, '//*[@id="id_birth_date"]').send_keys("")
driver.find_element(By.XPATH, '//*[@id="id_password1"]').send_keys("")
driver.find_element(By.XPATH, '//*[@id="id_password2"]').send_keys("")
driver.find_element(By.XPATH, '//*[@id="id_street_address"]').send_keys("Banasree")
driver.find_element(By.XPATH, '//*[@id="id_city"]').send_keys("Dhaka")
driver.find_element(By.XPATH, '//*[@id="id_postal_code"]').send_keys("1219")
driver.find_element(By.XPATH, '//*[@id="id_country"]').send_keys("Bangladesh")



driver.find_element(By.XPATH, '//*[@id="main"]/div/div/form/div[7]/button').click()

print("Registration Is Successfull")

time.sleep(5)
driver.close()

