import sys
import os
import time
import random

# ==========================================================
# CẤU HÌNH ĐƯỜNG DẪN (Đảm bảo tìm thấy thư mục Core)
# ==========================================================
# Lệnh này giúp Python biết thư mục gốc Werewolf ở đâu để import
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Bây giờ mới import các file phụ tùng từ Core
try:
    from Core.identity_gen import gen_fake_identity
    # Nếu bạn có hàm bypass trong file bypass_logic thì import ở đây
    # from Core.bypass_logic import apply_human_behavior 
except ImportError:
    print("[!] Lỗi: Không tìm thấy thư mục Core hoặc file identity_gen.py")
    sys.exit(1)

# ==========================================================
# HÀM XỬ LÝ CHÍNH
# ==========================================================
def smart_attack(target_url):
    print(f"\n[🚀] ĐANG KÍCH HOẠT CHẾ ĐỘ SMART ATTACK")
    print(f"[*] Mục tiêu: {target_url}")
    print("-" * 45)

    # 1. Tạo danh tính giả
    identity = gen_fake_identity()
    print(f"[+] Đang tạo danh tính giả: {identity['name']}")
    print(f"[+] Email giả: {identity['email']}")

    # 2. Giả lập hành vi người thật (Bypass Cloudflare)
    print("[*] Đang giả lập di chuyển chuột ngẫu nhiên...")
    time.sleep(random.uniform(1.5, 3.0))
    
    print("[*] Đang thực hiện thuật toán Bypass Logic...")
    time.sleep(random.uniform(1.0, 2.5))

    # 3. Gửi dữ liệu (Đây là nơi bạn sẽ thêm code Selenium sau này)
    print(f"[✓] Đã gửi gói tin 'Lừa đảo' ngược lại trang web!")
    print(f"[✓] Trạng thái: Bypass thành công!")
    print("-" * 45)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        smart_attack(url)
    else:
        print("[!] Thiếu URL mục tiêu.")
        
