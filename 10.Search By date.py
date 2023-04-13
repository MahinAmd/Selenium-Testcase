from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/accounts/login/")

driver.maximize_window()


driver.find_element(By.ID, "id_username").send_keys("iahmed.mahin@gmail.com")
driver.find_element(By.ID, "id_password").send_keys("pop12345")
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/form/div[3]/button').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="search"]').send_keys("01/04/2023")





time.sleep(5)
driver.close()

