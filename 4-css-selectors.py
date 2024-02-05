from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://syntaxprojects.com/basic-first-form-demo.php")

driver.implicitly_wait(5)

sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(By.ID, 'sum2')

# send all keyboard combinations
sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(40)


btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
btn.click()
