import time
from config import LOGIN_URL
from .login_actions.config import create_waiter, create_new_action_chain, new_driver_make
from .login_actions.utils import check_session_expired, retry_until_success
from .login_actions.form_actions import email_filed_filling, password_fill, cookie_accept, navigation_sense, sign_in, get_site_key_from_js
from .login_actions.captcha_solve import solve_turnstile, inject_turnstile_token

chrome_driver = new_driver_make(headless_=False)
waiter = create_waiter(chrome_driver, wait_time=30)
actions = create_new_action_chain(chrome_driver)

chrome_driver.get(LOGIN_URL)

retry_until_success(email_filed_filling, 5, "saidjalol1908@gmail.com", chrome_driver, waiter, actions)
retry_until_success(password_fill, 5, "Passw0rd!", chrome_driver, waiter, actions)
retry_until_success(cookie_accept, 5, chrome_driver, waiter, actions)

save_page_screenshot = chrome_driver.save_screenshot("screenshot_login.png")
sing_in_button = sign_in(chrome_driver,waiter,actions)




time.sleep(200)
chrome_driver.close()

