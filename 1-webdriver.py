# webdriver is a simulation that opens a web browser
# if we want to replicate the chrome browser we can import
# the class that simulates the chrome browser to perform
# automated tasks
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome, Firebox, Edge all are present
# Chromedriver needs to be installed 
# Chromedriver is a seperate executable file
# that the webdriver uses
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

# we dont really need to wait 30 second, it waits for 30s
# to load the page
# this is more efficient than time.sleep(30)
# it is going to be set as a timeout throught the selenium project
# so once we have set implicitly_wait as a certain time it becomes
# default throughtout the project everytime we try to get an element
driver.implicitly_wait(8)
download_button = driver.find_element(By.ID, 'downloadButton')
download_button.click()

# #this will give error that no such element has been found
# test_element = driver.find_element(By.ID, 'dsnfjd')

progress_element = driver.find_element(By.CLASS_NAME, 'progress-label')
# this will always return false because we need to wait for the 
# download progress bar to load completey
print(f"{progress_element.text == 'Complete!'} ")
