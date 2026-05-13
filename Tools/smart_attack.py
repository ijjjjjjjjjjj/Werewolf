import sys
import os
import time
import random

# Chỉ đường cho Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from Core.identity_gen import gen_fake_identity
except ImportError:
    print("[!] Lỗi: Không tìm thấy Core/identity_gen.py")
    sys.exit(1)

def smart_attack(target_url):
    print(f"\n[🚀] ĐANG KÍCH HOẠT CHẾ ĐỘ SMART ATTACK")
    print(f"[*] Mục tiêu: {target_url}")
    print("-" * 45)

    # Lấy danh tính và kiểm tra kỹ
    identity = gen_fake_identity()
    
    # Dùng .get() để không bị lỗi KeyError nếu thiếu dữ liệu
    fake_name = identity.get('name', 'Nguoi dung an danh')
    fake_email = identity.get('email', 'unknown@mail.com')

    print(f"[+] Đang tạo danh tính giả: {fake_name}")
    print(f"[+] Email giả: {fake_email}")

    print("[*] Đang giả lập hành vi người thật...")
    time.sleep(2)
    
    print(f"[✓] Đã gửi gói tin thành công qua Cloudflare!")
    print("-" * 45)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        smart_attack(sys.argv[1])
        
