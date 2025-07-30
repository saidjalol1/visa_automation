import time
from config import LOGIN_URL
from actions.config import get_driver, create_new_action_chain, create_waiter
from actions.utils import check_session_expired, retry_until_success
from actions.form_actions import email_filed_filling, password_fill, cookie_accept, navigation_sense, sign_in


def login(email, password):
    chrome_driver = get_driver()
    waiter = create_waiter(chrome_driver, 60)
    actions = create_new_action_chain(chrome_driver)
    chrome_driver.get(LOGIN_URL)

    
    email_filed_filling(email, chrome_driver, waiter, actions)
    password_fill(password, chrome_driver, waiter, actions)
    cookie_accept(chrome_driver, waiter, actions)
    sign_in(chrome_driver,waiter,actions)
    save_page_screenshot = chrome_driver.save_screenshot("screenshot_login.png")

    
    return False

def register(**data):
    pass
    return True


retry_until_success(login, 5, "saidjalol1908@gmail.com", "Passw0rd!")


    



    