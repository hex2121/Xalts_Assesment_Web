
node_id_field = "//span[text()='Node ID']//parent::legend//parent::fieldset//parent::div/input"

public_ip_field = "//span[text()='Public IP']//parent::legend//parent::fieldset//parent::div/input"

add_node_button = "//button[text()='+ Add Node ']"

next_button = "//button[text()='Next']"

wallet_address_field = "//label[text()='Wallet Address']//parent::div/div/input"

add_wallet_button = "//button[text()=' + Add Wallet ']"

submit_button = "//button[text()='Submit']"

updated_node_value = lambda x:f"//div[text()='{x}']"