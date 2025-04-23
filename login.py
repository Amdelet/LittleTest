import requests
import os

url = os.getenv("LOGIN_URL")
website = os.getenv("HOSTNAME")
accounts_raw = os.getenv("ACCOUNTS")
accounts = accounts_raw.split("|") if accounts_raw else []

session = requests.Session()
session.get(url)  # 设置 testcookie

for i, account in enumerate(accounts, 1):
    try:
        username, password = account.split(":")
    except ValueError:
        print(f"[{i}] 格式错误，跳过：{account}")
        continue

    payload = {
        "log": username,
        "pwd": password,
        "redirect_to": website,
        "testcookie": "1"
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": url
    }

    try:
        response = session.post(url, data=payload, headers=headers)
        if "注销" in response.text or "logout" in response.text.lower():
            print(f"[{i}] {username} Login success.")
            time.sleep(60)
        else:
            print(f"[{i}] {username} Login failed. 状态码：{response.status_code}")
            time.sleep(60)
    except Exception as e:
        print(f"[{i}] {username} 出错：{e}")
        time.sleep(60)
