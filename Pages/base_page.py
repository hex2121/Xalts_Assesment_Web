from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
"""
BasePage class that provides common functionality for all page objects.
Includes utility methods for waiting for elements to be clickable or visible.
"""
class BasePage:
    def __init__(self, driver):
        """
           Initialize the page object with a Selenium WebDriver instance.

           :param driver: Selenium WebDriver instance
        """
        self.driver = driver

    def wait_for_clickable(self, locator, timeout=10):
        """
            Wait until the element specified by locator is clickable.

            :param locator: Tuple (By.<METHOD>, 'value')
            :param timeout: Maximum time to wait (in seconds)
            :return: WebElement if clickable
        """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_visibility(self, locator, timeout=10):
        """
            Wait until the element specified by locator is visible.

            :param locator: Tuple (By.<METHOD>, 'value')
            :param timeout: Maximum time to wait (in seconds)
            :return: WebElement if visible
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


    def is_element_present(self, by, value):
        """
           Check if the element specified by the locator is present on the page with explicit wait.

           :param driver: The WebDriver instance controlling the browser
           :param by: Locator strategy (e.g., By.ID, By.XPATH)
           :param value: The locator value (e.g., 'submit-button', '//div[@class="msg"]')
           :return: True if element is present, False otherwise
           """
        try:
            # Use explicit wait to wait for the element to be present for up to 10 seconds
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by, value))
            )
            return True
        except Exception as e:
            a = e
            return False

    def is_button_disabled(self, by, value):
        """
        Checks if the button is disabled.

        :param driver: WebDriver instance
        :param by: Locator strategy (e.g., By.XPATH, By.ID)
        :param value: The value for the locator (e.g., 'submit-button', '//*[@id="submit"]')
        :return: True if the button is disabled, False if it's enabled
        """
        try:
            # Find the button element using the passed locator
            button = self.driver.find_element(by, value)

            # Check if the 'disabled' attribute is present and not None
            return button.get_attribute("disabled") is not None
        except Exception as e:
            print(f"An error occurred: {e}")
            return False  # Return False if there is any error

    def get_text_from_element(self, locator):
        """Get text from an element identified by the locator"""
        try:
            time.sleep(1)
            element = self.wait_for_visibility(locator)
            if element:
                return element.text.strip()  # Strip any leading/trailing whitespace
            return None
        except Exception as e:
            print(f"Error getting text from element: {str(e)}")
            return None