#!/bin/bash

# --- TỰ ĐỘNG SỬA LỖI ĐỊNH DẠNG (Quan trọng cho người dùng Windows/Linux) ---
sed -i 's/\r$//' start.sh 2>/dev/null
sed -i 's/\r$//' Core/*.py 2>/dev/null
sed -i 's/\r$//' Tools/*.py 2>/dev/null

G='\033[0;32m'
Y='\033[0;33m'
R='\033[0;31m'
NC='\033[0m'

clear
echo -e "${G}==============================================${NC}"
echo -e "${G}      WEREWOLF ANTI-FRAUD TOOLKIT V1          ${NC}"
echo -e "${G}==============================================${NC}"
echo -e "${Y}[!] Đang tự động tối ưu hóa hệ thống...${NC}"

# 1. Tự động cài đặt thư viện
echo -e "${Y}[*] Đang kiểm tra và cài đặt thư viện...${NC}"
pip install -r requirements.txt --quiet
echo -e "${G}[✓] Môi trường đã sẵn sàng!${NC}"

echo ""
read -p "Nhập URL trang web lừa đảo: " target

# 2. Phân tích mục tiêu
echo -e "${Y}[*] Đang phân tích mục tiêu bằng Core/Check.py...${NC}"
status=$(python3 Core/Check.py "$target")

echo -e "[!] Kết quả: ${G}$status${NC}"
echo "----------------------------------------------"

# 3. Kích hoạt vũ khí
if [ "$status" == "NORMAL" ]; then
    echo -e "${G}[-->] Web yếu! Đang tấn công...${NC}"
    python3 Tools/fast_spam.py "$target"
elif [ "$status" == "CLOUDFLARE_DETECTED" ] || [ "$status" == "CAPTCHA_DETECTED" ]; then
    echo -e "${Y}[-->] Web bảo vệ cao! Đang dùng Smart Attack...${NC}"
    python3 Tools/smart_attack.py "$target"
else
    echo -e "${R}[!] Không thể kết nối hoặc lỗi lạ.${NC}"
fi
