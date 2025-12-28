#https://humanbenchmark.com/tests/reactiontime botu ortalama 20 ms.

import mss
import time
import win32api
import win32con

target_pos = (1150, 480)
target_rgb = (75, 219, 106)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

# İlk başta hemen bir kere tıklasın
click(*target_pos)

# Ardından renk kontrolüne geçsin
with mss.mss() as sct:
    monitor = {"top": target_pos[1], "left": target_pos[0], "width": 1, "height": 1}
    while True:
        img = sct.grab(monitor)
        pixel = img.pixel(0, 0)
        if pixel == target_rgb:
            click(*target_pos)
            break  
