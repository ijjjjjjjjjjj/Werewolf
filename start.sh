#!/bin/bash
clear
echo "--- WEREWOLF ULTIMATE V3: CHIẾN THUẬT TỪNG DÒNG ---"
pip install requests colorama --quiet
read -p "Nhập link mục tiêu: " target
cd ~/Werewolf/Tools
python smart_attack.py "$target"
