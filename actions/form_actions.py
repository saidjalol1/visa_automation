import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .utils import human_sleep, retry_login_page
import time




def email_filed_filling(email, driver, wait, actions, input_id="email"):
    try:
        email_input = wait.until(EC.presence_of_element_located((By.ID, input_id)))
        actions.move_to_element(email_input).click().perform()
        human_sleep()
        
        for char in email:
            email_input.send_keys(char)
        save_page_screenshot = driver.save_screenshot("screenshot.png")
        print("Email typed.")
        return True
    except Exception as e:
        save_page_screenshot = driver.save_screenshot("screenshot.png")
        return False
    

def password_fill(password, driver, wait, actions, input_id="password"):
    try:
        password_input = wait.until(EC.presence_of_element_located((By.ID, input_id)))
        actions.move_to_element(password_input).click().perform()
        human_sleep()

        for char in password:
            password_input.send_keys(char)

        print("Password typed.")
        return True
    except Exception as e:
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
        save_page_screenshot = driver.save_screenshot("screenshot_login.png")
        return False

def sign_in(driver, wait, actions, text="Sign In"):
    try:
        print("Waiting for Sign In button...")
        sign_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[.//span[contains(text(), '{text}')]]")))

        if sign_in_btn.is_displayed():
            actions.move_to_element(sign_in_btn).pause(random.uniform(0.3, 0.7)).click().perform()
            print("Sign In button clicked.")
        return True
    except Exception as e:
        return False

def navigation_sense(driver, wait, actions, URL):
    try:
        wait.until(EC.url_changes(URL))
        driver.save_screenshot("screenshot.png")
        print("Navigation successful! Current URL:", driver.current_url)
        return True
    except Exception as e:
        driver.save_screenshot("screen_shot_otp.png")
        return False
    

def select_dial_code(driver, waiter, actions):
    # Click on the mat-select element
    dial_code_dropdown = waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'mat-select[formControlName="dialcode"]')))
    actions.move_to_element(dial_code_dropdown).pause(random.uniform(0.3, 0.7)).click().perform()

    # Wait for mat-option to appear
    waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'mat-option')))

   
    options = waiter.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "mat-option")))

    for opt in options:
        if "Uzbekistan" in opt.text.strip():
            actions.move_to_element(opt).pause(random.uniform(0.3, 0.7)).click().perform()
            break

    return True
    

def check_consent_checkboxes(driver, wait, actions, checkbox_count=3):
    try:
        checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        checked = 0

        for checkbox in checkboxes:
            if checked >= checkbox_count:
                break

            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", checkbox)
            time.sleep(random.uniform(0.3, 0.6))

            if not checkbox.is_selected() and checkbox.is_enabled():
                actions.move_to_element(checkbox).pause(random.uniform(0.3, 0.7)).click().perform()
                checked += 1
                time.sleep(random.uniform(0.4, 1.2))

        return True
    except Exception as e:
        print(f"Error while checking checkboxes: {e}")
        return False
    