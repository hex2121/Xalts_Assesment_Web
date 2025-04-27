# Xalts Assessment Web Automation

This project is an automated test suite for web application workflows using Selenium WebDriver and Pytest. It covers user authentication (sign up, sign in, sign out), node onboarding, and launching a private blockchain network.

## Features

- Automated UI tests for:
  - Sign Up
  - Sign In
  - Sign Out
  - Node Onboarding
  - Launching a new blockchain network
- Page Object Model structure for maintainability
- Screenshot capture on test failures
- Directory management for test artifacts

## Project Structure

- `Pages/` - Page Object classes for each web page
- `tests/` - Pytest test cases for each workflow
- `Config/` - Configuration and environment variables
- `Utilities/` - Utility functions (e.g., random string, screenshot)
- `requirements.txt` - Python dependencies

## Setup

1. **Clone the repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

## Running

- **Running the Tests**
   ```bash
   pytest
