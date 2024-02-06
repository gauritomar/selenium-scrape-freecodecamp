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

        for currency_button in currency_buttons:
            if "USD" in currency_button.text:
                currency_button.click()
                print("Selected USD as Currency")
                break

        else:
            print("Button containing text 'USD' not found")

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, ':re:')
        search_field.clear()

        search_field.send_keys(place_to_go)

        first_element = self.find_element(By.CSS_SELECTOR, 
            '#autocomplete-result-0'
        )
        first_element.click()

        print("Clicked on the first autocomplete of dropdown")

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, 
            f'[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        print("Selected check in date")

        check_out_element = self.find_element(By.CSS_SELECTOR,
            f'[data-date="{check_out_date}"]'
        )
        check_out_element.click()
        print("Selected check out date")

    def select_adults(self, count):
        occupancy_button = self.find_element(By.CSS_SELECTOR, '[data-testid="occupancy-config"]')
        occupancy_button.click()
        print("Select Occupancy Button")

        decrease_adult = self.find_element(By.CSS_SELECTOR, '[class*="bb803d8689"][class*="e91c91fa93"]')
        decrease_adult.click()

        print("Decreased adults")
        spans = self.find_elements(By.CSS_SELECTOR, 'span.d723d73d5f')
        span_values = [span.text for span in spans]
        print("Values of spans: ", span_values)

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR,
            'button[type="submit"]'
        )

        search_button.click()
    
    