import random
import time

def human_delay():
    """Tạo khoảng nghỉ ngẫu nhiên như người thật đang suy nghĩ"""
    time.sleep(random.uniform(0.5, 2.0))

def get_random_offset(size):
    """Tính toán điểm click lệch nhẹ (như bạn yêu cầu)"""
    # Lệch trong khoảng 1/4 kích thước của nút bấm
    offset = random.randint(-int(size/4), int(size/4))
    return offset

def typing_slow(element, text):
    """Giả vờ gõ phím chậm từng chữ một"""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))
      
