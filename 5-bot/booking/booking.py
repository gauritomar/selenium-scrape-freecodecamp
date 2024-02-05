from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import booking.constant as const

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.driver = webdriver.Chrome()
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        try:
            self.get(const.BASE_URL)
            sign_in_popup = self.find_element(By.CLASS_NAME, 'c0528ecc22')
            dismiss_button = self.find_element(By.CSS_SELECTOR, '[aria-label="Dismiss sign in information."]')
            dismiss_button.click()
            print("Clicked on Dismiss sign in information")
        except NoSuchElementException:
            print("Sign-in popup not found or already dismissed.")
            pass
    
    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR,
            'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()

        currency_buttons = selected_currency_element = self.find_elements(
            By.CSS_SELECTOR,
            'button[data-testid="selection-item"]'
        )

        print("Currency Buttons: ", currency_buttons)

        for currency_button in currency_buttons:
            print(currency_button.text)
            # i want to choose 
