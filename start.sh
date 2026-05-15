#!/bin/bash
# Tự động cài đặt môi trường
echo "[*] Đang tối ưu hóa môi trường Termux..."
pkg update -y && pkg install python -y
pip install grequests requests colorama beautifulsoup4

# Cấp quyền thực thi cho chính nó và file python
chmod +x start.sh
chmod +x smart_attack.py

clear
echo "==============================================="
echo "   WEREWOLF ULTIMATE - SCAM DESTROYER v2.0"
echo "        3 PHƯƠNG ÁN TẤN CÔNG TỔNG LỰC"
echo "==============================================="
read -p "Nhập link web lừa đảo (VD: https://abc.com): " target
python smart_attack.py "$target"
