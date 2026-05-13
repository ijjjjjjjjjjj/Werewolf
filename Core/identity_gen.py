import random

def gen_fake_identity():
    # Danh sách dữ liệu mẫu
    names = ["Nguyen Van A", "Tran Thi B", "Le Van C", "Hoang Minh D"]
    domains = ["gmail.com", "outlook.com", "yahoo.com"]
    
    name = random.choice(names)
    # Tạo email từ tên (viết liền, không dấu)
    email_name = name.lower().replace(" ", "") + str(random.randint(100, 999))
    email = f"{email_name}@{random.choice(domains)}"
    
    # Trả về một Dictionary có key là 'name' và 'email'
    return {
        "name": name,
        "email": email
    }
    
