from pyautogui import write, press
import time

def spam(input, n):
    for i in range(n):
        write(input)
        press('enter')

#main
time.sleep(3)
spam("You're an idiot", 100)