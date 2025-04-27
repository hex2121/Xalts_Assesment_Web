import pytest
from Pages.node_onboarding_page import NodeOnboardingPage
from Utilities.project_utils import *
from Config.config import *
from Pages.signin_page import SigninPage

@pytest.mark.usefixtures("browser")
class TestNodeOnboarding:
    """Test suite for NodeOnboarding functionality."""

    def test_node_onboarding_positive(self, browser):
        """Test successful Node Onboarding"""
        signin_page = SigninPage(browser)
        signin_page.load(website_link)
        signin_page.signin_with_correct_cred(static_correct_email, correct_password)
        nodeonboarding_page = NodeOnboardingPage(browser)
        nodeonboarding_page.reach_onboarding_page()
        result = nodeonboarding_page.onboarding_node_to_existing_blockchain_positive(correct_nodeid, correct_ip, correct_wallet_address)
        if result[0] == 'Fail':
            take_screenshot(browser, "test_node_onboarding_positive")

        assert result[0] == "Pass", f"test_node_onboarding_positive failed: '{result[1]}'"