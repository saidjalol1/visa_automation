from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium_stealth import stealth
import time
from config import TOR_PROXY

def get_chrome_options(headless=False):
    options = ChromeOptions()
    
    options.add_argument(f'--proxy-server={TOR_PROXY}')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    
   
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    
    return options

def set_initial_cookies(driver, domain):
    driver.get("https://www.google.com")
    time.sleep(2) 
    


def new_driver_make(headless_=False, target_domain=None):
    options = get_chrome_options(headless_)
    driver = Chrome(options=options, headless=headless_)
    
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    

    if target_domain:
        set_initial_cookies(driver, target_domain)
    
    return driver

def setup_stealth(driver):
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win64",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            run_on_insecure_origins=True
    )


def initialize_driver(headless=True, target_domain=".example.com"):
    driver = new_driver_make(headless_=headless, target_domain=target_domain)
    setup_stealth(driver)
    driver.get("https://www.google.com")
    driver.save_screenshot("test_init.png")
    
    return driver

def create_new_action_chain(driver):
    return ActionChains(driver)

def create_waiter(driver, wait_time=30):
    return WebDriverWait(driver, wait_time)