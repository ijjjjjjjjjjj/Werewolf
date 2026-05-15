#!/bin/bash
clear
echo "==============================================="
echo "   WEREWOLF ULTIMATE - SCAM DESTROYER v2.0"
echo "        3 PHƯƠNG ÁN TẤN CÔNG TỔNG LỰC"
echo "==============================================="
read -p "Nhập link mục tiêu: " target

# Bước quan trọng: Di chuyển vào thư mục chứa code
cd ~/Werewolf/Tools

# Chạy tool với link mục tiêu đã nhập
python smart_attack.py "$target"
