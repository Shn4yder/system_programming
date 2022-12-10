# Пожалуйста, проверьте и предыдущие задания, если Вам не составит труда:)
import time
from threading import Thread
import socket
#Потоки

def remind():
    print("Введите напоминание")
    text = str(input())
    print("Через сколько минут его вывести?")
    text_time = float(input())
    time.sleep(text_time * 60)
    print(text)
th = Thread(target=remind, args=())
th.start()
time.sleep(10)
print("Подождите пока поток работает\nПрограммист знает тайны Вселенной всей,\nОн имеет огромную силу.\nОн путь нужный отыщет мышкой своей,\nИ найдёт золотую жилу.\n")

#Клиент
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "83.221.209.6"
PORT = 80
connection.connect((IP, PORT))
rd = connection.recv(1024)
print(rd.decode('utf8'))
connection.send("Сообщение серверу".encode('utf8'))
connection.close()

#Хэш-таблица.Словарь представляет собой хеш-таблицу и называется ассоциативным массивом
name = input("Введите имя пользователя: ")
data = {"John": 56411,
        "Mike": 12122,
        "Anna": 94120,
        "Nick": 97444}
for key, value in data.items():
    if name in key:
        print(value)
        break
else:
    print("Пользователь не найден")