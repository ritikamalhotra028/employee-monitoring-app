# modules/activity_monitor.py
from pynput import mouse, keyboard

def on_move(x, y):
    print(f"Mouse moved to {(x, y)}")

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at {(x, y)}")

def on_key_press(key):
    print(f"Key pressed: {key}")

def monitor_activity():
    with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
        with keyboard.Listener(on_press=on_key_press) as listener2:
            listener.join()
            listener2.join()
