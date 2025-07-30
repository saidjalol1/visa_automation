# config.py
import sqlite3
import os
from pathlib import Path



# Urls settings
LOGIN_URL = "https://visa.vfsglobal.com/uzb/en/ltp/login"
REGISTER_URL = "https://visa.vfsglobal.com/uzb/en/ltp/register"

# Tor settings
TOR_PROXY = "socks5://127.0.0.1:9050"
# Proxy server
PROXY_HOST = "p.welchbar.e.io" 
PROXY_PORT = "9999"              
SOURCE_IP = "94.230.230.209"

# Browser settings
HEADLESS = True
RETRY_INTERVAL = 60  
FILE_PATH = "SHABLON8.xlsx"
PROFILE_DIR = os.path.join(os.getcwd(), "playwright_profile")


# Databse Configurations
DB_FILE = "users.db"
database_connection = sqlite3.connect(DB_FILE, check_same_thread=False)
cursor = database_connection.cursor()



""" API configurations """
# Rapid api vs Temp mail confs
RAPIDAPI_KEY = "c34c51da20msh541b3eab9bf3ffep13745fjsn56b38b8c6684"
RAPIDAPI_HOST = "tempmail-api-free.p.rapidapi.com"
BASE_URL = f"https://{RAPIDAPI_HOST}/api/v3/email/new"

HEADERS = {
    "Content-Type": "application/json",
    "x-rapidapi-host": RAPIDAPI_HOST,
    "x-rapidapi-key": RAPIDAPI_KEY
}

DOMAIN = "wywnxa.com"


# Bright Data API
BRIGHT_DATA_API_KEY = "86a783fadec6b8a297a66411742ab4dab31b0559d2d51802b0d2fa59635987c0"
