import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium_stealth import stealth
import time
from config import TOR_PROXY
import zipfile
import os

proxy_server = {
    "username":"crnrnfav-rotate",
    "password":"hasurniwkmo2",
    "server":"p.webshare.io:80"
}

def create_proxy_extension(proxy_host, proxy_port, proxy_user, proxy_pass):
    """Creates a Chrome proxy extension"""
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        }
    }
    """
    
    background_js = """
    var config = {
        mode: "fixed_servers",
        rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: %d
            },
            bypassList: ["localhost"]
        }
    };
    
    chrome.proxy.settings.set(
        {value: config, scope: "regular"}, 
        function() {}
    );
    
    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }
    
    chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        {urls: ["<all_urls>"]},
        ['blocking']
    );
    """ % (proxy_host, proxy_port, proxy_user, proxy_pass)
    
    os.makedirs("proxy_extension", exist_ok=True)
    with open("proxy_extension/manifest.json", "w") as f:
        f.write(manifest_json)
    with open("proxy_extension/background.js", "w") as f:
        f.write(background_js)
    
    with zipfile.ZipFile("proxy_extension.zip", "w") as zf:
        zf.write("proxy_extension/manifest.json", "manifest.json")
        zf.write("proxy_extension/background.js", "background.js")
    
    return "proxy_extension.zip"

def get_chrome_options(headless=False):
    options = uc.ChromeOptions()
   
    proxy_host, proxy_port = proxy_server["server"].split(":")
    proxy_extension = create_proxy_extension(
        proxy_host,
        int(proxy_port),
        proxy_server["username"],
        proxy_server["password"]
    )
    options.add_extension(proxy_extension)
 
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-dev-shm-usage") 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    
    return options

def set_initial_cookies(driver, domain):
    driver.get("https://www.google.com")
    time.sleep(2) 
    


def new_driver_make(headless_=False, target_domain=None):
    options = get_chrome_options(headless_)
    driver = uc.Chrome(options=options, headless=headless_)
    
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