# modules/background_tasks.py
import threading
import time
from modules.screenshot import capture_screenshot
from modules.aws_upload import upload_to_s3

def start_monitoring(interval, capture_enabled, blur_enabled, bucket_name):
    def capture_and_upload():
        while capture_enabled:
            file_name = capture_screenshot(blur=blur_enabled)
            upload_to_s3(file_name, bucket_name, os.path.basename(file_name))
            time.sleep(interval * 60)
    
    thread = threading.Thread(target=capture_and_upload)
    thread.daemon = True
    thread.start()
