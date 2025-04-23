import requests
import os

# 登录接口地址（请根据实际网站修改）
url = "https://www.ttloli.com/wp-login.php"
# 从环境变量获取账号列表
accounts_raw = os.getenv("ACCOUNTS")
accounts = accounts_raw.split("|") if accounts_raw else []

session = requests.Session()
session.get(url)

for i, account in enumerate(accounts, 1):
    try:
        username, password = account.split(":")
    except ValueError:
        print(f"[{i}] 格式错误，跳过：{account}")
        continue

    payload = {
        "log": username,
        "pwd": password,
        "redirect_to": "https://www.ttlloli.com",  # 可选
        "testcookie": "1"
    }
    
    headers = {
    "User-Agent": "Mozilla/5.0"
    }

    try:
        response = session.post(url, data=payload, headers=headers)  
        if "注销" in response.text or "logout" in response.text.lower():
            print(f"[{i}] {username} Login success.")
        else:
            print(f"[{i}] {username} Login failed.")
    except Exception as e:
         print("An error occurred:", e)
