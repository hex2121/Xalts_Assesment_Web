import pytest
from Pages.launch_ocn_page import LaunchOcnPage
from Utilities.project_utils import *
from Config.config import *
from Pages.signin_page import SigninPage

@pytest.mark.usefixtures("browser")
class TestLaunchOCN:
    """Test suite for NodeOnboarding functionality."""

    def test_launch_new_blockchain_positive(self, browser):
        """Test successful Node Onboarding"""
        signin_page = SigninPage(browser)
        signin_page.load(website_link)
        signin_page.signin_with_correct_cred(static_correct_email, correct_password)
        nodeonboarding_page = LaunchOcnPage(browser)
        nodeonboarding_page.reach_child_net_launch_page()
        result = nodeonboarding_page.create_new_private_blockchain_positive(network_name, correct_wallet_address, correct_ip, correct_nodeid)
        if result[0] == 'Fail':
            take_screenshot(browser, "test_launch_new_blockchain_positive")

        assert result[0] == "Pass", f"test_launch_new_blockchain_positive failed: '{result[1]}'"