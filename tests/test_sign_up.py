import pytest
from Pages.signup_page import SignupPage
from Config.config import *
from Utilities.project_utils import *

@pytest.mark.usefixtures("browser")
class TestSignUp:
    """Test suite for Sign Up functionality."""

    def test_signup_positive(self, browser):
        """Test successful sign up with valid credentials."""
        page = SignupPage(browser)
        page.load(website_link)
        result = page.signup_with_correct_cred(email_random, correct_password)
        if result[0] == 'Fail':
            take_screenshot(browser, "test_signup_positive")


        assert result[0] == "Pass", f"test_signup_positive failed: '{result[1]}'"

    def test_signup_invalid_email(self, browser):
        """Test sign up with invalid email."""
        page = SignupPage(browser)
        page.load(website_link)
        result = page.signup_incorrect_format_email(incorrect_email, correct_password)
        if result[0] == 'Fail':
            take_screenshot(browser, "test_signup_invalid_email")
        assert result[0] == "Pass", f"test_signup_invalid_email failed: '{result[1]}'"

    def test_signup_invalid_password(self, browser):
        """Test sign up with invalid password."""
        page = SignupPage(browser)
        page.load(website_link)
        result = page.signup_incorrect_format_password(static_correct_email, incorrect_password)
        if result[0] == 'Fail':
            take_screenshot(browser, "test_signup_invalid_email")
        assert result[0] == "Pass", f"test_signup_invalid_email failed: '{result[1]}'"

    def test_signup_password_and_confirm_password_dont_match(self, browser):
        """Test sign up with invalid password."""
        page = SignupPage(browser)
        page.load(website_link)
        result = page.signup_passwords_dont_match(static_correct_email, correct_password, correct_password2)
        if result[0] == 'Fail':
            take_screenshot(browser, "test_signup_password_and_confirm_password_dont_match")
        assert result[0] == "Pass", f"test_signup_password_and_confirm_password_dont_match failed: '{result[1]}'"