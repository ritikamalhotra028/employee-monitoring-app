# modules/screenshot.py
import pyautogui
from PIL import Image, ImageFilter
import time
import os

def capture_screenshot(blur=False, output_dir="assets/"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    screenshot = pyautogui.screenshot()
    if blur:
        screenshot = screenshot.filter(ImageFilter.GaussianBlur(5))
    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{output_dir}/screenshot_{timestamp}.png"
    screenshot.save(filename)
    return filename
