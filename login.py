import requests
import os

# 登录接口地址（请根据实际网站修改）
url = "https://www.ttloli.com/wp-login.php"

# 从环境变量获取账号列表
accounts_raw = os.getenv("ACCOUNTS")
accounts = accounts_raw.split("|") if accounts_raw else []

for i, account in enumerate(accounts, 1):
    try:
        username, password = account.split(":")
    except ValueError:
        print(f"[{i}] 格式错误，跳过：{account}")
        continue

    data = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(url, json=data)
        if response.ok:
            print(f"[{i}] {username} 登录成功")
        else:
            print(f"[{i}] {username} 登录失败: {response.status_code} {response.text}")
    except Exception as e:
        print(f"[{i}] {username} 登录异常: {e}")
