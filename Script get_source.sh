#!/bin/bash
read -p "Nhập URL mục tiêu để lấy code: " target
curl -s "$target" > savehack.txt
echo "[✓] Đã tải toàn bộ code về savehack.txt"
echo "[!] Bây giờ hãy dùng lệnh: nano savehack.txt để sửa theo ý bạn."

