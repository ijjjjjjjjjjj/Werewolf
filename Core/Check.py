import requests
import sys

def check_web(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        
        server = response.headers.get('Server', '').lower()
        content = response.text.lower()

        if "cloudflare" in server or "cf-ray" in response.headers:
            return "CLOUDFLARE_DETECTED"
        elif "captcha" in content or "verify you are human" in content:
            return "CAPTCHA_DETECTED"
        elif response.status_code == 403:
            return "IP_BLOCKED"
        else:
            return "NORMAL"
    except Exception as e:
        return f"ERROR: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(check_web(sys.argv[1]))
      
