import time
from config import LOGIN_URL
from .login_actions.config import create_waiter, create_new_action_chain, new_driver_make,initialize_driver
from .login_actions.utils import check_session_expired, retry_until_success
from .login_actions.form_actions import email_filed_filling, password_fill, cookie_accept, navigation_sense, sign_in, get_site_key_from_js
from utils.tor_execution import run_tor, wait_for_tor_proxy


tor_run = run_tor()
status = wait_for_tor_proxy()

if status:
    chrome_driver = initialize_driver(headless=True)
    waiter = create_waiter(chrome_driver, wait_time=30)
    actions = create_new_action_chain(chrome_driver)
    
    chrome_driver.get("https://httpbin.org/ip")
    chrome_driver.save_screenshot("verify_proxy.png")
    
    chrome_driver.get(LOGIN_URL)

    retry_until_success(email_filed_filling, 5, "saidjalol1908@gmail.com", chrome_driver, waiter, actions)
    retry_until_success(password_fill, 5, "Passw0rd!", chrome_driver, waiter, actions)
    retry_until_success(cookie_accept, 5, chrome_driver, waiter, actions)

    sing_in_button = sign_in(chrome_driver,waiter,actions)
    time.sleep(10)
    save_page_screenshot = chrome_driver.save_screenshot("screenshot_login.png")




    time.sleep(200)
    chrome_driver.close()

