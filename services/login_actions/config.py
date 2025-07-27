from undetected_chromedriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


def new_driver_make(proxy: str = None, headless_: bool = False):
    chrome = Chrome(headless=headless_)
    return chrome


def create_new_action_chain(driver):
    actions = ActionChains(driver)
    return actions


def create_waiter(driver, wait_time : int = 30):
    wait = WebDriverWait(driver, wait_time)
    return wait
