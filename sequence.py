import pyautogui
import time
from PIL import ImageGrab

pyautogui.PAUSE = 0
pyautogui.MINIMUM_DURATION = 0


def safe_click(x, y, hold_time=0):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    time.sleep(hold_time)
    pyautogui.mouseUp()

# Başlangıç koordinatları ve grid yapısı
start_x, start_y = 800, 400
cell_spacing = 163
grid_coords = [(start_x + col * cell_spacing, start_y + row * cell_spacing)
               for row in range(3) for col in range(3)]

white_color = (255, 255, 255)

# Başlangıç tıklaması
print("990,700 konumuna tıklanıyor...")
safe_click(990, 700)
time.sleep(0.5)

# Önceki renkleri kaydet
previous_colors = [ImageGrab.grab().load()[x, y] for x, y in grid_coords]

# Aşama bilgileri
step = 0
current_step_sequence = []
last_sequence = []
step_ready_time = None  # Yeni aşama algılandığında zaman kaydedilir

print("Beyaz hücreler izleniyor...")

while True:
    image = ImageGrab.grab()
    pixels = image.load()

    for idx, (x, y) in enumerate(grid_coords):
        color = pixels[x, y]

        if color == white_color and previous_colors[idx] != white_color:
            print(f"Aşama {step}: Hücre {idx} beyaza döndü.")
            current_step_sequence.append(idx)

        previous_colors[idx] = color

    # Aşama hazır hale geldiyse ve zaman henüz kaydedilmediyse
    if (len(current_step_sequence) > len(last_sequence) and
        current_step_sequence[:-1] == last_sequence and
        step_ready_time is None):
        step_ready_time = time.time()
        print(f"Aşama {step} hazırlandı. 0.5 saniye bekleniyor...")

    # Zaman dolduysa tıklamalara başla
    if step_ready_time is not None and (time.time() - step_ready_time >= 0.5):
        print(f"Aşama {step}: Tıklamalar başlıyor -> {current_step_sequence}")
        for i in current_step_sequence:
            cx, cy = grid_coords[i]
            safe_click(cx, cy)
            time.sleep(0.1)

        # Aşama tamamlandı
        step += 1
        last_sequence = current_step_sequence[:]
        current_step_sequence = []
        step_ready_time = None

    time.sleep(0.05)
