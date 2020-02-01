
import arduino
import telegram
from time import sleep

while True:
    comand = telegram.get_my_posts()
    my_arduino = arduino.Arduino('test')

    print(f">>> Comando recebido pelo Telegram: {comand}")

    my_arduino.set(comand)

