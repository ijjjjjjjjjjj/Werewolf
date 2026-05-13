import time
import random
from Core.identity_gen import gen_fake_identity
from Core.bypass_logic import apply_human_behavior # Giả sử bạn có hàm này trong file bypass

def start_smart_attack(url):
    print(f"[+] Đang khởi động chế độ người dùng giả lập cho: {url}")
    
    # Lấy danh tính giả từ Core/identity_gen.py
    identity = gen_fake_identity()
    
    print(f"[*] Sử dụng danh tính: {identity['name']} - {identity['email']}")
    
    # Giả lập các bước di chuột và gõ phím từ bypass_logic
    print("[*] Đang di chuyển chuột ngẫu nhiên để vượt Cloudflare...")
    time.sleep(random.uniform(2, 4)) 
    
    print("[*] Đang nhập liệu chậm (giống người thật)...")
    # Ở đây sau này bạn sẽ thêm code Selenium để điền form tự động
    
    print("[✓] Đã gửi dữ liệu rác thành công!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        start_smart_attack(sys.argv[1])
      
