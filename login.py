import requests
import os

# 获取环境变量中的账号密码（从 GitHub Secrets 注入）
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# 登录接口（根据目标网站修改）
url = "https://example.com/api/login"

# 请求体内容（根据接口要求修改）
data = {
    "username": username,
    "password": password
}

# 发起登录请求
response = requests.post(url, json=data)

if response.ok:
    print("登录成功")
else:
    print("登录失败:", response.status_code, response.text)
