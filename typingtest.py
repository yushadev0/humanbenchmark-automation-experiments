import pyautogui
import time
import unicodedata
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selenium: Debugging moduna bağlan
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)

# letters notranslate div'ini bul
wait = WebDriverWait(driver, 10)
letters_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".letters.notranslate")))
spans = letters_div.find_elements(By.TAG_NAME, "span")

# textContent ile tüm harfleri topla
raw_text = ''.join([span.get_attribute("textContent") for span in spans])

# Unicode normalize: özel boşluk karakterleri → normal boşluk
text = raw_text.replace('\u00A0', ' ')  # kırılmaz boşluk → normal boşluk
text = unicodedata.normalize("NFKC", text)  # Unicode karakterleri sadeleştir

# Kontrol için yazdır
print("Yazılacak metin:", text)
print(f"Uzunluk: {len(text)} karakter")

# 3 saniye sonra yazmaya başla
print("3 saniye içinde input alanına tıkla...")
time.sleep(3)

# PyAutoGUI ile yaz
pyautogui.write(text, interval=0.01)  
