import http.client
import json
import re
import requests
from config import RAPIDAPI_KEY, RAPIDAPI_HOST
from bs4 import BeautifulSoup

conn = http.client.HTTPSConnection("tempmail-api-free.p.rapidapi.com")
headers = {
    'x-rapidapi-key': RAPIDAPI_KEY,
    'x-rapidapi-host': RAPIDAPI_HOST
}

def get_email(email):
    conn.request("GET", f"/api/v3/email/{email}/messages", headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data)
    return data


def activate_account(email):
    emails = json.loads(get_email(email))

    if not emails:
        print("No emails received for:", email)
        return

    email_data = emails[0]
    
    raw_html = email_data.get("body_html", "")
    raw_text = email_data.get("body_text", "")
    
    if raw_html.strip():
        soup = BeautifulSoup(raw_html, "html.parser")
        readable_text = soup.get_text(separator="\n").strip()
        print("Email (HTML -> Text):\n", readable_text)
        search_source = raw_html
    else:
        print("Email (Plain Text):\n", raw_text.strip())
        search_source = raw_text

    match = re.search(r'https://row1\.vfsglobal\.com/User/ActivateAccount\?[^"\s<]+', search_source)

    if not match:
        print("Activation link not found.")
        return

    activation_link = match.group(0)
    print("\n🔗 Found activation link:\n", activation_link)

    try:
        response = requests.get(activation_link, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            print("✅ VFS account activated.")
        else:
            print(f"Activation failed. Status code: {response.status_code}")
    except Exception as e:
        print("Error while sending activation request:", str(e))
        

# activate_account("f12kv3s9@daouse.com")