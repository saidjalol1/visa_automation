import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .utils import human_sleep, retry_login_page
import time




def email_filed_filling(email, driver, wait, actions):
    try:
        email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
        actions.move_to_element(email_input).click().perform()
        human_sleep()
        
        for char in email:
            email_input.send_keys(char)
            human_sleep(0.05, 2)
        save_page_screenshot = driver.save_screenshot("screenshot_login.png")
        print("Email typed.")
        return True
    except Exception as e:
        print("Email input failed:", e)
        save_page_screenshot = driver.save_screenshot("screenshot_login.png")
        return False
    


def password_fill(password, driver, wait, actions):
    try:
        password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
        actions.move_to_element(password_input).click().perform()
        human_sleep()

        for char in password:
            password_input.send_keys(char)
            human_sleep(0.05, 2)

        print("Password typed.")
        return True
    except Exception as e:
        print("Password input failed:", e)
        save_page_screenshot = driver.save_screenshot("screenshot_login.png")
        return False
        

def cookie_accept(driver,wait, actions):
    try:
        print("Waiting for cookie consent button...")
        cookie_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Accept Only Necessary')]")))
        if cookie_button.is_displayed() and cookie_button.is_enabled():
            actions.move_to_element(cookie_button).pause(random.uniform(0.3, 0.6)).click().perform()
            print("Cookie consent accepted.")
        return True
    except Exception as e:
        print("No cookie prompt visible or already accepted.")
        save_page_screenshot = driver.save_screenshot("screenshot_login.png")
        return False

def sign_in(driver, wait, actions):
    try:
        print("Waiting for Sign In button...")
        sign_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Sign In')]]")))

        if sign_in_btn.is_displayed():
            actions.move_to_element(sign_in_btn).pause(random.uniform(0.3, 0.7)).click().perform()
            print("Sign In button clicked.")
        return True
    except Exception as e:
        print("Sign In click failed:", e)
        return False

def navigation_sense(driver, wait, actions, URL):
    try:
        wait.until(EC.url_changes(URL))
        driver.save_screenshot("screenshot.png")
        print("Navigation successful! Current URL:", driver.current_url)
        return True
    except Exception as e:
        print("No URL change detected.")
        driver.save_screenshot("screen_shot_otp.png")
        return False
        

def get_site_key_from_js(driver):
    script = """
    try {
        return window._cf_chl_opt && window._cf_chl_opt.chlApiSitekey;
    } catch (e) {
        return null;
    }
    """
    sitekey = driver.execute_script(script)
    if sitekey:
        print(f"[INFO] Extracted sitekey from JS: {sitekey}")
    else:
        print("[ERROR] Sitekey not found in _cf_chl_opt")
    
    print(sitekey)
    return sitekey