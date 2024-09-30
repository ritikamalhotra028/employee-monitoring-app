# main.py
import tkinter as tk
from modules.gui import MonitoringApp
from modules.background_tasks import start_monitoring
from modules.activity_monitor import monitor_activity

def start_monitoring_callback(interval, capture_enabled, blur_enabled):
    bucket_name = "your-s3-bucket-name"
    print(f"Starting monitoring: interval={interval}, capture_enabled={capture_enabled}, blur_enabled={blur_enabled}")
    start_monitoring(interval, capture_enabled, blur_enabled, bucket_name)
    monitor_activity()

if __name__ == "__main__":
    root = tk.Tk()
    app = MonitoringApp(root, start_monitoring_callback)
    root.mainloop()
