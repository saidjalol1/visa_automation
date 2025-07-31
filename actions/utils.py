import time
import random
import sys


def human_sleep(a=0.2, b=0.6):
    time.sleep(random.uniform(a, b))
    

def check_session_expired(driver):
    return "Session Expired" in driver.page_source or "page-not-found" in driver.current_url


def retry_login_page(driver, max_attempts=3):
    for attempt in range(max_attempts):
        if check_session_expired(driver):
            print(f"Session expired (Attempt {attempt+1}/{max_attempts}). Retrying...")
            driver.delete_all_cookies()
            driver.refresh()
            human_sleep(2, 4)
        else:
            return True
    print("Session could not be recovered.")
    

def retry_until_success(func, *args, **kwargs):
    while True:
        try:
            result = func(*args, **kwargs)
            if result:
                return True
            else:
                print("Attempt failed. Retrying...")
        except Exception as e:
            print(f"Exception occurred: {e}. Retrying...")
        time.sleep(3)


def check_values(values):
    if all(values):
        return True
    return False