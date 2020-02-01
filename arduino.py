
import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

class Arduino:

    model = "Arduino Mega"

    # Initializer / Instance Attributes
    def __init__(self, model):
        self.model = model

    # instance method
    def set(self, option):

        if option == "On":
            board.digital[13].write(1)

        elif option == "Off":
            board.digital[13].write(0)

if __name__ == "__main__":
    set_arduino("On")
