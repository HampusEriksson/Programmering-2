import random
import time

from pynput.keyboard import Key, Controller

keyboard = Controller()


while True:
    time.sleep(random.random())
    keyboard.press("a")
    keyboard.release("a")