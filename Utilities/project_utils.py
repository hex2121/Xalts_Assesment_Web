import random
import string
import os
from pathlib import Path

def random_string(length=8):
    """
    Generate a random string of lowercase letters.

    :param length: Length of the generated string (default is 8)
    :return: A random string of the specified length
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def take_screenshot(driver, test_name):
    script_dir = Path(__file__).parent

    parent_dir = script_dir.parent
    screenshots_dir = f"{parent_dir}/Data/ErrorScreenshot"

    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    # Define the screenshot path
    screenshot_path = os.path.join(screenshots_dir, f"{test_name}_failure.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")