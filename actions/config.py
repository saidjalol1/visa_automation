import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

def get_driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--no-first-run")
    options.add_argument("--no-service-autorun")
    
    return uc.Chrome(
        options=options,
        headless=False,
        use_subprocess=True,
        no_sandbox=True,
        suppress_welcome=True,
        disable_crash_upload=True,
    )

def create_new_action_chain(driver):
    return ActionChains(driver)

def create_waiter(driver, wait_time=30):
    return WebDriverWait(driver, wait_time)