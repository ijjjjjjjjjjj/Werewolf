# Werewolf
Tool Anti-fraud
Please hack the scammer.
# 🐺 Werewolf Anti-Scam Toolkit

Công cụ tự động phân tích và bơm dữ liệu rác vào các trang web lừa đảo.

## 🛠️ Hướng dẫn cài đặt và sử dụng

Nếu bạn mới tải tool về, hãy thực hiện các lệnh sau trong Terminal (hoặc Termux) để kích hoạt:

1. **Tải công cụ về máy:**
   ```bash
   git clone https://github.com/ijjjjjjjjjjj/Werewolf.git
cd Werewolf

### Tại sao làm vậy là "đàng hoàng"?
1.  **Chủ động sửa lỗi:** Người dùng không cần biết `sed` là gì, file `start.sh` sẽ tự "dọn rác" cho họ ngay khi vừa chạy.
2.  **Hướng dẫn `chmod +x`:** Đây là bước quan trọng nhất. Nếu không có dòng này trong `README.md`, người khác tải về gõ `./start.sh` sẽ bị báo `Permission denied` (Truy cập bị từ chối) và họ sẽ tưởng tool hỏng.
3.  **Giao diện trực quan:** Khi có `README.md`, kho code của bạn trên GitHub trông sẽ chuyên nghiệp hơn hẳn, giống như một sản phẩm hoàn thiện.
### 🛠️ Cách khắc phục lỗi "bad interpreter" hoặc "^M"
Nếu bạn chạy `./start.sh` mà báo lỗi, hãy copy và chạy lệnh này nếu như chạy xong thì chỉ cần bấm lại ./start.sh nó sẽ trả lời bình thường 

```bash
sed -i 's/\r$//' start.sh && echo "Đã sửa lỗi định dạng thành công!
