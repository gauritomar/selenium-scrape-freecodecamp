'''
This file will include a class with instance methods
responsible for interacting with our website after we
have some results to apply filtrations
'''
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self):
        # label element for 5 stars
        label_element = self.driver.find_element(By.CSS_SELECTOR, 'label[for=":r25:"]')
        
        # span element inside the label element
        span_element = label_element.find_element(By.CSS_SELECTOR, 'span.ff5328eb35')
        span_element.click()

        print("Applied the 5star+ label")
