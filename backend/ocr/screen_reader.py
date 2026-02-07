import pytesseract
import pyautogui
import cv2
import numpy as np

# 🔴 REQUIRED ON WINDOWS
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def capture_screen():
    """
    Capture a specific screen region
    (x, y, width, height)
    """
    x, y, width, height = 100, 200, 800, 400

    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    image = np.array(screenshot)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def extract_text(image):
    custom_config = r'--oem 3 --psm 6'
    return pytesseract.image_to_string(image, config=custom_config)

def capture_and_read():
    image = capture_screen()
    text = extract_text(image)
    return text.strip()

if __name__ == "__main__":
    print("📸 Capturing screen...")
    print("🔍 OCR output:\n")
    print(capture_and_read())
