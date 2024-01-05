from pyautogui import write, press
import time

def spam(input, n):
    for i in range(n):
        write(input)
        press('enter')

#main
line = input("Enter message : ")
n = int(input("Enter no. of times : "))
time.sleep(4)
spam(line, n)