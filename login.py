import requests
import os

url = "https://www.ttloli.com/wp-login.php"
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
        "redirect_to": "https://www.ttloli.com",
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
        else:
            print(f"[{i}] {username} Login failed. 状态码：{response.status_code}")
    except Exception as e:
        print(f"[{i}] {username} 出错：{e}")
