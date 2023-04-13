from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
driver.maximize_window()


driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys("mahin@admin.com")
driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys("mahin12345")
driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="user-tools"]/a[3]').click()





time.sleep(2)
driver.close()

