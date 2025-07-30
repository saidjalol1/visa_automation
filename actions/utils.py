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
    

def retry_until_success(func, max_retries=3, *args, **kwargs):
    for attempt in range(max_retries):
        result = func(*args, **kwargs)
        if result:
            return True
        print(f"Retrying {func.__name__} (attempt {attempt + 1}/{max_retries})")
    return False
