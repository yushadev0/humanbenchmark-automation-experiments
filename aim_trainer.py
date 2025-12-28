# https://humanbenchmark.com/tests/aim ortalama 100ms de çözen bir program.


import pyautogui
from PIL import ImageGrab
import numpy as np
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0
pyautogui.MINIMUM_DURATION = 0


# Tarama alanı
x1, y1 = 343, 279
x2, y2 = 1556, 812

# Aranacak ana renk
target_color = (149, 195, 232)

# Durma sinyali için kontrol konumu ve rengi
stop_x, stop_y = 915, 730
stop_color = (255, 209, 84)

# Başlangıç tıklaması
time.sleep(0.5)
pyautogui.click(950, 548)
print("Başlangıç tıklaması yapıldı. Tarama başlıyor...")

def should_stop():
    # Belirtilen koordinattaki piksel rengi kontrol edilir
    pixel_color = pyautogui.pixel(stop_x, stop_y)
    return pixel_color == stop_color

def find_and_click_fast():
    # Belirtilen alanı yakala
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    img_np = np.array(img)

    # RGB kanallarını ayıkla
    rgb = img_np[:, :, :3]

    # Renk eşleşmeleri
    match = np.all(rgb == target_color, axis=2)

    if np.any(match):
        y_indices, x_indices = np.where(match)
        first_match_x = x_indices[0]
        first_match_y = y_indices[0]

        screen_x = x1 + first_match_x
        screen_y = y1 + first_match_y + 40  # 40 pixel aşağısı

        pyautogui.moveTo(screen_x, screen_y)
        pyautogui.click()
        print(f"Tıklandı: ({screen_x}, {screen_y})")
        return True
    return False

# Ana döngü
try:
    while True:
        # Durdurma sinyali kontrolü
        if should_stop():
            print(f"Durdurma rengi ({stop_color}) {stop_x},{stop_y} noktasında algılandı. Program sonlandırıldı.")
            break

        if not find_and_click_fast():
            print("Hedef renk bulunamadı. Tarama sonlandırıldı.")
            break
except KeyboardInterrupt:
    print("Kullanıcı tarafından durduruldu.")
