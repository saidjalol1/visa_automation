import time
from config import REGISTER_URL
from actions.config import get_driver, create_new_action_chain, create_waiter
from actions.utils import check_session_expired, retry_until_success
from actions.form_actions import email_filed_filling, password_fill, cookie_accept, navigation_sense, sign_in, select_dial_code, check_consent_checkboxes
from utils.db_commands import fetch_all_users_as_dict
from test import activate_account
from config import DB_FILE

def register():
    chrome_driver = get_driver()
    waiter = create_waiter(chrome_driver)
    actions = create_new_action_chain(chrome_driver)
    chrome_driver.get(REGISTER_URL)
    users = fetch_all_users_as_dict(DB_FILE)
    print(users[0])
    
    email_filled = email_filed_filling(users[0].get("email"), chrome_driver, waiter, actions, "inputEmail")
    password_filled = password_fill(users[0].get("password"), chrome_driver, waiter, actions)
    password_confirm = password_fill(users[0].get("password"), chrome_driver, waiter, actions, "confirmPassword")
    phone_number_fill = password_fill(users[0].get("phone")[3:12], chrome_driver, waiter, actions, "mat-input-3")
    cookie_accepted = cookie_accept(chrome_driver, waiter, actions)
    select_dial = select_dial_code(chrome_driver, waiter, actions)
    check_box = check_consent_checkboxes(chrome_driver, waiter, actions)
    sing_in_button_clicked = sign_in(chrome_driver,waiter,actions, "Register")
    
    if all([
        email_filled,
        password_filled,
        password_confirm,
        phone_number_fill,
        cookie_accepted,
        select_dial,
        check_box,
        sing_in_button_clicked,
    ]):
        email_activate_inp = email_filed_filling(users[0].get("email"), chrome_driver, waiter, actions, "mat-input-4")
        activate_btn = sign_in(chrome_driver,waiter,actions, "Activate")
        if activate_btn and email_activate_inp:
            save_page_screenshot = chrome_driver.save_screenshot("screenshot_login.png")
            # activate_account("f12kv3s9@daouse.com")
        else:
            return False
        time.sleep(60)
        return True
    return False

retry_until_success(register, 5)




    



    