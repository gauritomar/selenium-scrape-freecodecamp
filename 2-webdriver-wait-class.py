import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

driver.implicitly_wait(8)
download_button = driver.find_element(By.ID, 'downloadButton')
download_button.click()

print("Clicked on the download button.")

# Initialise the web driver wait class and pass in our object
# along with how much time we would want to wait
try:
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element(
            # Element filtration
            (By.CLASS_NAME, 'progress-label'),
            'Complete!'  # The expected text
        )
    )
    print("Download completed successfully.")
except Exception as e:
    print(f"Error: {e}")

# EC: Expected Conditions has a lot of methods
