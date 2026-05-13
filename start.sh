#!/bin/bash

# Sửa lỗi xuống dòng để chạy được trên mọi hệ điều hành
sed -i 's/\r$//' start.sh 2>/dev/null
sed -i 's/\r$//' Core/*.py 2>/dev/null
sed -i 's/\r$//' Tools/*.py 2>/dev/null

# Màu sắc giao diện
G='\033[0;32m'
Y='\033[0;33m'
R='\033[0;31m'
NC='\033[0m'

clear
echo -e "${G}==============================================${NC}"
echo -e "${G}      WEREWOLF ANTI-FRAUD TOOLKIT             ${NC}"
echo -e "${G}==============================================${NC}"

# Tự động cài đặt thư viện cần thiết
echo -e "${Y}[*] Đang kiểm tra môi trường...${NC}"
pip install -r requirements.txt --quiet

echo ""
read -p "Nhập URL trang web lừa đảo: " target

# GỌI FILE - CHÚ Ý: Chữ 'C' trong 'Core' và 'Check.py' phải viết hoa
echo -e "${Y}[*] Đang phân tích mục tiêu bằng Core/Check.py...${NC}"
status=$(python3 Core/Check.py "$target")

echo -e "[!] Kết quả phân tích: ${G}$status${NC}"
echo "----------------------------------------------"

# QUYẾT ĐỊNH VŨ KHÍ - CHÚ Ý: Chữ 'T' trong 'Tools' phải viết hoa
if [ "$status" == "NORMAL" ]; then
    echo -e "${G}[-->] Web yếu! Khởi động tấn công tốc độ cao...${NC}"
    python3 Tools/fast_spam.py "$target"
elif [ "$status" == "CONNECTION_FAILED" ] || [ "$status" == "TIMEOUT" ]; then
    echo -e "${R}[!] Lỗi: Không thể kết nối đến web mục tiêu.${NC}"
else
    echo -e "${Y}[!] Trạng thái: $status. Cần dùng chế độ Smart Attack.${NC}"
fi
