# modules/gui.py
import tkinter as tk
from tkinter import ttk

class MonitoringApp:
    def __init__(self, root, start_monitoring_callback):
        self.root = root
        self.start_monitoring_callback = start_monitoring_callback
        
        # GUI Elements
        self.root.title("Employee Monitoring App")
        
        ttk.Label(self.root, text="Screenshot Interval (minutes):").grid(row=0, column=0, padx=10, pady=5)
        self.interval_var = tk.IntVar(value=5)
        ttk.Entry(self.root, textvariable=self.interval_var).grid(row=0, column=1, padx=10, pady=5)

        self.capture_enabled_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.root, text="Enable Screenshot Capture", variable=self.capture_enabled_var).grid(row=1, column=0, padx=10, pady=5)

        self.blur_enabled_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(self.root, text="Blur Screenshots", variable=self.blur_enabled_var).grid(row=2, column=0, padx=10, pady=5)

        ttk.Button(self.root, text="Start Monitoring", command=self.start_monitoring).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def start_monitoring(self):
        interval = self.interval_var.get()
        capture_enabled = self.capture_enabled_var.get()
        blur_enabled = self.blur_enabled_var.get()
        self.start_monitoring_callback(interval, capture_enabled, blur_enabled)
