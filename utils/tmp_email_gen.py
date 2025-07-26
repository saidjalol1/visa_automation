import requests
import random
import string
import time
from config import RAPIDAPI_HOST, RAPIDAPI_KEY, BASE_URL, DOMAIN, HEADERS


def generate_password():
    """Valid password generator for accounts"""
    length = random.randint(8, 15)
    
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice('$@#!%*?')

    
    all_chars = string.ascii_letters + string.digits + '$@#!%*?'

   
    remaining_length = length - 4
    remaining_chars = random.choices(all_chars, k=remaining_length)

   
    password_list = list(upper + lower + digit + special) + remaining_chars
    random.shuffle(password_list)
    
    return ''.join(password_list)


def generate_random_name(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def create_temp_email():
    name = generate_random_name()
    payload = {
        "domain": DOMAIN,
        "name": name
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(f"✅ Created: {name}@{DOMAIN}")
        print(response.json())
        return response.json()
    else:
        print(f"Failed ({response.status_code}): {response.text}")
        return None
