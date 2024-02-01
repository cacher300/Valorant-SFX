import tkinter as tk
from tkinter import simpledialog
from screeninfo import get_monitors


def create_monitor_window(monitor, number):
    window = tk.Tk()
    window.title(f" {number}")
    window.geometry(f"200x100+{monitor.x}+{monitor.y}")
    label = tk.Label(window, text=f" {number}", font=("Arial", 24))
    label.pack(expand=True)
    return window


def display_numbers_on_monitors():
    monitors = get_monitors()
    windows = []
    for i, monitor in enumerate(monitors):
        win = create_monitor_window(monitor, i)
        windows.append(win)

    root = tk.Tk()
    root.withdraw()
    choice = simpledialog.askinteger("Monitor Selection", "Enter the monitor number you want to use:")

    for win in windows:
        win.destroy()

    root.destroy()

    return choice


def get_dynamic_region_for_selected_monitor(monitor):
    x_percent = 2735 / 3456
    y_percent = 758 / 2160
    width_percent = (3408 - 2735) / 3456
    height_percent = (1395 - 795) / 2160

    x_start = int(x_percent * monitor.width)
    y_start = int(y_percent * monitor.height)
    width = int(width_percent * monitor.width)
    height = int(height_percent * monitor.height)

    region = (x_start, y_start, width, height)
    return region


def real():
    choice = display_numbers_on_monitors()
    monitors = get_monitors()
    if choice is not None and choice < len(monitors):
        selected_monitor = monitors[choice]
    else:
        print("No selection made or invalid selection. Defaulting to the primary monitor.")
        selected_monitor = monitors[0]

    region = get_dynamic_region_for_selected_monitor(selected_monitor)
    return region

