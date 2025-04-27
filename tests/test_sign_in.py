import pytest
from Pages.signin_page import SigninPage
from Utilities.project_utils import *
from Config.config import *

@pytest.mark.usefixtures("browser")
class TestSignIn:
    """Test suite for Sign In functionality."""

    def test_signin_positive(self, browser):
        """Test successful sign in with valid credentials."""
        page = SigninPage(browser)
        page.load(website_link)
        result = page.signin_with_correct_cred(static_correct_email, correct_password)
        if result[0] == 'Fail':
            take_screenshot(browser, "test_signin_positive")

        assert result[0] == "Pass", f"test_signin_positive failed: '{result[1]}'"

    def test_signin_invalid_email(self, browser):
        """Test sign up with invalid email."""
        page = SigninPage(browser)
        page.load(website_link)
        result = page.signin_incorrect_format_email(incorrect_email, correct_password)
        if result[0] == 'Fail':
            take_screenshot(browser, "test_signin_invalid_email")
        assert result[0] == "Pass", f"test_signin_invalid_email failed: '{result[1]}'"

    def test_signin_invalid_password(self, browser):
        """Test sign up with invalid password."""
        page = SigninPage(browser)
        page.load(website_link)
        result = page.signin_incorrect_format_password(static_correct_email, incorrect_password)
        if result[0] == 'Fail':
            take_screenshot(browser, "test_signin_invalid_password")
        assert result[0] == "Pass", f"test_signin_invalid_password failed: '{result[1]}'"
