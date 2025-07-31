import time
from config import REGISTER_URL
from actions.config import get_driver, create_new_action_chain, create_waiter
from actions.utils import  retry_until_success, check_values
from actions.form_actions import (email_filed_filling, 
                                  password_fill, 
                                  cookie_accept, 
                                  sign_in, 
                                  select_dial_code, 
                                  check_consent_checkboxes, 
                                  check_registration_success
                                  )

from utils.db_commands import fetch_all_users_as_dict
from test import activate_account
from config import DB_FILE
import logging


logging.basicConfig(
    filename='registration_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def register():
    chrome_driver = get_driver()
    waiter = create_waiter(chrome_driver,10)
    actions = create_new_action_chain(chrome_driver)
    logging.info(f"Requested {REGISTER_URL}")
    chrome_driver.get(REGISTER_URL)
    users = fetch_all_users_as_dict(DB_FILE)
    
    logging.info(f"Attempting to register user: {users[2].get('email')}")
    email_filled = email_filed_filling(users[2].get("email"), chrome_driver, waiter, actions, "inputEmail")
    password_filled = password_fill(users[2].get("password"), chrome_driver, waiter, actions)
    password_confirm = password_fill(users[2].get("password"), chrome_driver, waiter, actions, "confirmPassword")
    phone_number_fill = password_fill(users[2].get("phone")[3:12], chrome_driver, waiter, actions, "mat-input-3")
    cookie_accepted = cookie_accept(chrome_driver, waiter, actions)
    select_dial = select_dial_code(chrome_driver, waiter, actions)
    check_box = check_consent_checkboxes(chrome_driver, waiter, actions)
    
    check_vals = check_values([
        email_filled,
        password_filled,
        password_confirm,
        phone_number_fill,
        cookie_accepted,
        select_dial,
        check_box])

    
    if not check_vals:
        return False
    
    sing_in_button_clicked = sign_in(chrome_driver,waiter,actions, "Register")
    success = check_registration_success(chrome_driver, waiter)
    if success:
        chrome_driver.save_screenshot(f"register_success/success_screen.png")
        return True
    
    screen_shot = chrome_driver.save_screenshot(f"register_test/register_test.png")
    chrome_driver.quit()
    return False

retry_until_success(register)




    



    