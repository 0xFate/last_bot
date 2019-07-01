import pyautogui
import time

print(pyautogui.size())

prev_x = 0
prev_y = 0

while True:
    x, y = pyautogui.position()
    if x != prev_x or y != prev_y:
        prev_x = x
        prev_y = y
        print("X: {0}; Y: {1}".format(x, y))

    time.sleep(1)
