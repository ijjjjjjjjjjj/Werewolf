#!/bin/bash

# Sửa lỗi định dạng dòng cho toàn bộ hệ thống
sed -i 's/\r$//' start.sh 2>/dev/null
sed -i 's/\r$//' Core/*.py 2>/dev/null
sed -i 's/\r$//' Tools/*.py 2>/dev/null

G='\033[0;32m'
Y='\033[0;33m'
R='\033[0;31m'
NC='\033[0m'

clear
echo -e "${G}==============================================${NC}"
echo -e "${G}      WEREWOLF ANTI-FRAUD TOOLKIT             ${NC}"
echo -e "${G}==============================================${NC}"

# 1. Tự động cài đặt thư viện
echo -e "${Y}[*] Đang kiểm tra môi trường...${NC}"
pip install -r requirements.txt --quiet

echo ""
read -p "Nhập URL trang web lừa đảo: " target

# 2. Phân tích mục tiêu (Gọi bộ não Core)
echo -e "${Y}[*] Đang phân tích mục tiêu bằng Core/Check.py...${NC}"
status=$(python3 Core/Check.py "$target")

echo -e "[!] Kết quả phân tích: ${G}$status${NC}"
echo "----------------------------------------------"

# 3. Kích hoạt vũ khí tương ứng
if [ "$status" == "NORMAL" ]; then
    echo -e "${G}[-->] Web yếu! Khởi động Fast Spammer...${NC}"
    python3 Tools/fast_spam.py "$target"

elif [ "$status" == "CLOUDFLARE_DETECTED" ] || [ "$status" == "CAPTCHA_DETECTED" ]; then
    echo -e "${Y}[-->] Web bảo vệ cao! Khởi động Smart Attack (Bypass)...${NC}"
    # ĐÃ MỞ KHÓA DÒNG NÀY:
    python3 Tools/smart_attack.py "$target"

elif [ "$status" == "CONNECTION_FAILED" ] || [ "$status" == "TIMEOUT" ]; then
    echo -e "${R}[!] Lỗi: Không thể kết nối đến web mục tiêu.${NC}"

else
    echo -e "${Y}[!] Cảnh báo: Trạng thái lạ ($status). Hãy kiểm tra thủ công.${NC}"
fi
