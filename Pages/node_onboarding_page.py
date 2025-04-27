from selenium.webdriver.common.by import By
from Locators.home_page_locators import *
from Pages.base_page import BasePage
from Locators.node_onboarding_page_locators import *
import time

class NodeOnboardingPage(BasePage):
    """Page Object for the NodeOnboarding functionality."""
    def __init__(self, driver):
        self.driver = driver

    def load(self, base_url):
        self.driver.get(f"{base_url}")

    def reach_onboarding_page(self):
        try:
            self.wait_for_visibility((By.XPATH, get_started_button)).click()
            self.wait_for_visibility((By.XPATH, onboarding_ocn_button)).click()
        except Exception as e:
            return "Fail", e
    def onboarding_node_to_existing_blockchain_positive(self, nodeid, ip_address, wallet_address):
        try:
            self.wait_for_visibility((By.XPATH, node_id_field)).send_keys(nodeid)
            self.wait_for_visibility((By.XPATH, public_ip_field)).send_keys(ip_address)
            self.wait_for_visibility((By.XPATH, add_node_button)).click()
            self.wait_for_visibility((By.XPATH, next_button)).click()
            self.wait_for_visibility((By.XPATH, wallet_address_field)).send_keys(wallet_address)
            self.wait_for_visibility((By.XPATH, add_wallet_button)).click()
            self.wait_for_visibility((By.XPATH, next_button)).click()
            time.sleep(2)
            result = self.is_element_present(By.XPATH, updated_node_value(nodeid))

            if result == True:
                return "Pass", result
            else:
                return "Fail", "Node was not present"



        except Exception as e:

            return "Fail", e

