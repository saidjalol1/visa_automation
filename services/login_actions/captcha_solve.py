import requests
import time

def solve_turnstile(api_key, site_key, page_url):
    url = "http://2captcha.com/in.php"
    payload = {
        "key": api_key,
        "method": "turnstile",
        "sitekey": site_key,
        "pageurl": page_url,
        "json": 1
    }
    response = requests.post(url, data=payload).json()

    if response.get("status") != 1:
        raise Exception("Failed to send CAPTCHA request:", response)

    request_id = response["request"]

    for _ in range(30):
        time.sleep(5)
        result = requests.get(
            f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"
        ).json()

        if result.get("status") == 1:
            return result["request"]
        elif result.get("request") != "CAPCHA_NOT_READY":
            raise Exception("Error from 2Captcha:", result)

    raise TimeoutError("CAPTCHA solving timed out")


def inject_turnstile_token(driver, token):
    script = '''
    const turnstileResponse = document.querySelector('input[name="cf-turnstile-response"]');
    if (turnstileResponse) {
        turnstileResponse.value = arguments[0];
        console.log("Turnstile token injected!");
    } else {
        console.error("Turnstile input not found!");
    }
    '''
    driver.execute_script(script, token)