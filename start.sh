#!/bin/bash
clear
echo "=============================================="
echo "      WEREWOLF ANTI-FRAUD TOOLKIT V1"
echo "=============================================="

# Cứ nhập vào thôi, không bắt bẻ gì cả
read -p "Nhập mục tiêu: " target

echo "[*] Đang phân tích: $target"

# Kiểm tra Cloudflare nhanh rồi chạy luôn
status=$(curl -I -s --max-time 3 "$target" | grep -i "server: cloudflare")

if [[ ! -z "$status" ]]; then
    python3 Tools/smart_attack.py "$target"
else
    python3 Tools/fast_spam.py "$target"
fi
