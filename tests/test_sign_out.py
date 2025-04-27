import pytest
from Pages.signout_page import SignoutPage
from Pages.signin_page import SigninPage
from Utilities.project_utils import *
from Config.config import *

@pytest.mark.usefixtures("browser")
class TestSignOut:
    """Test suite for Sign Out functionality."""

    def test_signout_positive(self, browser):
        """Test successful sign out after sign in."""
        signin_page = SigninPage(browser)
        signin_page.load(website_link)
        signin_page.signin_with_correct_cred(static_correct_email, correct_password)
        # Now, sign out
        signout_page = SignoutPage(browser)
        result = signout_page.signout()
        if result[0] == 'Fail':
            take_screenshot(browser, "test_signout_positive")

        assert result[0] == "Pass", f"test_signout_positive failed: '{result[1]}'"
