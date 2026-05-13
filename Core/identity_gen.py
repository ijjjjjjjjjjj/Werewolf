import random
import string

def gen_fake_identity():
    # Tạo tên ngẫu nhiên
    first_names = ["nguyen", "tran", "le", "pham", "hoang", "phan", "vu", "dang"]
    last_names = ["anh", "bao", "duy", "khoi", "minh", "nam", "tu", "vy"]
    name = random.choice(first_names) + random.choice(last_names) + str(random.randint(10, 99))
    
    # Tạo email giả
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    email = f"{name}@{random.choice(domains)}"
    
    # Tạo mật khẩu giả
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    
    # Danh sách User-Agent giả (Mặt nạ trình duyệt)
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15",
        "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36"
    ]
    
    return {
        "user": name,
        "email": email,
        "pass": password,
        "ua": random.choice(user_agents)
    }

if __name__ == "__main__":
    print(gen_fake_identity())
  
