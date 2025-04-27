from selenium.webdriver.common.by import By
from Locators.home_page_locators import *
from Pages.base_page import BasePage
from Locators.signin_page_locators import *

class SignoutPage(BasePage):
    """Page Object for the Sign Out functionality."""
    def __init__(self, driver):
        self.driver = driver

    def signout(self):
        try:
            signout_button = self.wait_for_visibility((By.XPATH, sign_out_button))
            signout_button.click()
            result = self.is_element_present(By.XPATH, sign_in_button)

            if result==True:
                return "Pass", result
            else:
                return "Fail", "Sign in button was not present"

        except Exception as e:

            return "Fail", e