#!/bin/bash

# Định nghĩa màu sắc
G='\033[0;32m'
R='\033[0;31m'
Y='\033[0;33m'
NC='\033[0m'

clear
echo -e "${G}=============================================="
echo -e "      WEREWOLF ANTI-FRAUD TOOLKIT V2"
echo -e "                    🐺
echo -e "==============================================${NC}"

# 1. Nhập và kiểm tra định dạng URL
echo -ne "${Y}[?] Nhập URL mục tiêu: ${NC}"
read target

# Kiểm tra nếu chuỗi nhập vào không bắt đầu bằng http
if [[ ! $target =~ ^https?:// ]]; then
    echo -e "${R}[!] LỖI: '$target' không phải là địa chỉ web!${NC}"
    echo -e "${Y}[i] URL hợp lệ phải có dạng: https://vi-du.com${NC}"
    exit 1
fi

echo -e "${G}[✓] Địa chỉ hợp lệ. Đang tiến hành phân tích...${NC}"
sleep 1

# 2. Phân tích bảo vệ (Cloudflare Check)
# Kiểm tra xem Server có trả về nhãn 'cloudflare' không
status=$(curl -I -s --max-time 5 "$target" | grep -i "server: cloudflare")

if [[ ! -z "$status" ]]; then
    echo -e "${R}[!] CẢNH BÁO: Phát hiện Cloudflare Protection!${NC}"
    echo -e "${Y}[-->] Chuyển hướng sang chế độ Smart Attack...${NC}"
    python3 Tools/smart_attack.py "$target"
else
    echo -e "${G}[+] Mục tiêu không có bảo vệ mạnh.${NC}"
    echo -e "${Y}[-->] Kích hoạt Fast Spam...${NC}"
    # Đảm bảo file fast_spam.py có tồn tại hoặc đổi tên theo đúng file bạn có
    python3 Tools/fast_spam.py "$target"
fi
