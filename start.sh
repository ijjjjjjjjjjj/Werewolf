#!/bin/bash

# --- Cấu hình màu sắc ---
G='\033[0;32m'
R='\033[0;31m'
Y='\033[0;33m'
NC='\033[0m'

clear
echo -e "${G}==============================================${NC}"
echo -e "${G}      werewolf anti-fraud.                    ${NC}"
echo -e "${G}==============================================${NC}"

# --- BƯỚC 1: KIỂM TRA & CÀI ĐẶT MÔI TRƯỜNG ---
echo -e "${Y}[*] Đang kiểm tra thư viện hệ thống...${NC}"
if [ -f "requirements.txt" ]; then
    # Cài đặt ẩn để giao diện trông sạch sẽ hơn
    pip install -r requirements.txt --quiet
    echo -e "${G}[✓] Môi trường đã sẵn sàng!${NC}"
else
    echo -e "${R}[!] Lỗi: Thiếu file requirements.txt ở thư mục gốc!${NC}"
    exit 1
fi

# --- BƯỚC 2: NHẬP MỤC TIÊU ---
echo ""
read -p "Nhập URL trang web lừa đảo: " target

# --- BƯỚC 3: TRINH SÁT (GỌI core/check.py) ---
echo -e "${Y}[*] Đang phân tích mục tiêu bằng core/check.py...${NC}"
# Lưu ý: Ở đây đã sửa từ checker.py thành check.py cho khớp với file của bạn
status=$(python3 core/check.py "$target")

echo -e "[!] Kết quả phân tích: ${G}$status${NC}"
echo "----------------------------------------------"

# --- BƯỚC 4: QUYẾT ĐỊNH PHƯƠNG ÁN TẤN CÔNG ---
if [ "$status" == "NORMAL" ]; then
    echo -e "${G}[-->] Web yếu! Khởi động Fast Spammer (Tốc độ cao)...${NC}"
    python3 tools/fast_spam.py "$target"

elif [ "$status" == "CLOUDFLARE_DETECTED" ] || [ "$status" == "CAPTCHA_DETECTED" ]; then
    echo -e "${Y}[-->] Web có bảo vệ! Đang chuẩn bị chế độ Smart Attack...${NC}"
    echo -e "${R}[!] Lưu ý: Chế độ này cần Selenium và Chrome Driver.${NC}"
    # Sau này bạn tạo file này xong thì mở lệnh dưới đây ra:
    # python3 tools/smart_attack.py "$target"

elif [ "$status" == "IP_BLOCKED" ]; then
    echo -e "${R}[!] Bạn đã bị web chặn IP (403). Hãy bật VPN hoặc đổi Proxy!${NC}"

elif [ "$status" == "CONNECTION_FAILED" ] || [ "$status" == "TIMEOUT" ]; then
    echo -e "${R}[!] Không thể kết nối. Có thể web đã sập hoặc link sai.${NC}"

else
    echo -e "${Y}[!] Cảnh báo: Trạng thái lạ ($status). Hãy kiểm tra thủ công.${NC}"
fi

