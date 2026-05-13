import requests
import sys

def check_web(url):
    # Thêm tiền tố http nếu người dùng quên nhập
    if not url.startswith('http'):
        url = 'https://' + url

    try:
        # Giả lập một trình duyệt thật để tránh bị chặn ngay lập tức
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        # Gửi yêu cầu thăm dò với timeout 10 giây
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        
        server = response.headers.get('Server', '').lower()
        content = response.text.lower()

        # Logic nhận diện hệ thống bảo vệ
        if "cloudflare" in server or "cf-ray" in response.headers:
            return "CLOUDFLARE_DETECTED"
        elif "captcha" in content or "verify you are human" in content:
            return "CAPTCHA_DETECTED"
        elif response.status_code == 403:
            return "IP_BLOCKED"
        elif response.status_code == 404:
            return "NOT_FOUND"
        else:
            return "NORMAL"

    except requests.exceptions.ConnectionError:
        return "CONNECTION_FAILED" # Web đã sập hoặc link sai
    except requests.exceptions.Timeout:
        return "TIMEOUT" # Web quá chậm
    except Exception as e:
        return f"UNKNOWN_ERROR" # Các lỗi phát sinh khác

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # In kết quả cuối cùng để file .sh đọc
        print(check_web(sys.argv[1]))
        
