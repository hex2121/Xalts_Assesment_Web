from selenium.webdriver.common.by import By
from Locators.signin_page_locators import *
from Pages.base_page import BasePage
from Locators.home_page_locators import *
import time

class SigninPage(BasePage):
    """Page Object for the Sign In page."""
    def __init__(self, driver):
        self.driver = driver

    def load(self, base_url):
        self.driver.get(f"{base_url}/signin")

    def signin_with_correct_cred(self, email, password):
        try:
            already_sign_in_button = self.is_element_present(By.XPATH, already_have_an_account_button)
            if already_sign_in_button:
                already_signin_button = self.wait_for_visibility((By.XPATH, already_have_an_account_button))
                already_signin_button.click()
            email_input_field = self.wait_for_visibility((By.XPATH, email_field))
            email_input_field.send_keys(email)
            password_input_field = self.wait_for_visibility((By.XPATH, password_field))
            password_input_field.send_keys(password)
            sign_up_but = self.wait_for_clickable((By.XPATH, sign_in_button))
            sign_up_but.click()
            result = self.is_element_present(By.XPATH, sign_out_button)

            if result == True:
                return "Pass", result
            else:
                return "Fail", "Sign out button not found"

        except Exception as e:

            return "Fail", e
    def signin_incorrect_format_email(self, email, password):
        try:
            already_sign_in_button = self.is_element_present(By.XPATH, already_have_an_account_button)
            if already_sign_in_button:
                already_signin_button = self.wait_for_visibility((By.XPATH, already_have_an_account_button))
                already_signin_button.click()
            email_input_field = self.wait_for_visibility((By.XPATH, email_field))
            email_input_field.send_keys(email)
            password_input_field = self.wait_for_visibility((By.XPATH, password_field))
            password_input_field.send_keys(password)
            time.sleep(2)
            result = self.is_button_disabled(By.XPATH, sign_in_button)

            if result==True:
                return "Pass", result
            else:
                return "Fail", "Sign out button was active"

        except Exception as e:

            return "Fail", e

    def signin_incorrect_format_password(self, email, password):
        try:
            already_sign_in_button = self.is_element_present(By.XPATH, already_have_an_account_button)
            if already_sign_in_button:
                already_signin_button = self.wait_for_visibility((By.XPATH, already_have_an_account_button))
                already_signin_button.click()
            email_input_field = self.wait_for_visibility((By.XPATH, email_field))
            email_input_field.send_keys(email)
            password_input_field = self.wait_for_visibility((By.XPATH, password_field))
            password_input_field.send_keys(password)
            time.sleep(2)
            result = self.is_element_present(By.XPATH, password_format_incorrect_text)

            if result==True:
                return "Pass", result
            else:
                return "Fail", "Sign out button was active"

        except Exception as e:

            return "Fail", e