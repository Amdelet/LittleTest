import requests
import os

# 登录接口地址（请根据实际网站修改）
url = "https://www.ttloli.com/wp-login.php"
session = requests.Session()
# 从环境变量获取账号列表
accounts_raw = os.getenv("ACCOUNTS")
accounts = accounts_raw.split("|") if accounts_raw else []

for i, account in enumerate(accounts, 1):
    try:
        username, password = account.split(":")
    except ValueError:
        print(f"[{i}] 格式错误，跳过：{account}")
        continue

    payload = {
        "username": username,
        "password": password
    }

    try:
        response = requests.session(url, data=payload, timeout=3)
    if "Logout" in response.text:
        print(f"[{i}] {username} Login success.")
    else:
        print(f"[{i}] {username} Login failed.")
