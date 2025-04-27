import os
from dotenv import load_dotenv
from Utilities.project_utils import random_string
from pathlib import Path

load_dotenv()

website_link = os.getenv("site_link")

script_dir = Path(__file__).parent

parent_dir = script_dir.parent


# Generate a unique email using a random string
email_random = f"{random_string()}@example.com"
correct_password = os.getenv("password")
correct_password2 = f"{correct_password}ABC"

static_correct_email = "bltxrnxx@example.com"

incorrect_email = "bltxrnxx"
incorrect_password = "1234asdf"

correct_nodeid = f"NodeID-{random_string()}"
incorrect_nodeid = "IncorrectNodeID"

correct_ip = "192.1.1.1"
incorrect_ip = "IncorrectIP"

correct_wallet_address = "0x88fa61d2faA13aad8Fbd5B030372B4A159BbbDFb"

network_name = "testName"



