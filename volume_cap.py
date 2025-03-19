import time
import threading
import tkinter as tk
import sys
import socket
import pickle
import os
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL, CoInitialize
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

PORT = 65432
volume_cap = 0.10
running = True

BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
SETTINGS_FILE = os.path.join(BASE_DIR, "volume_cap_settings.txt")

def save_settings():
    try:
        with open(SETTINGS_FILE, "w") as f:
            f.write(str(int(volume_cap * 100)))
    except:
        pass

def load_settings():
    global volume_cap
    try:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, "r") as f:
                val = int(f.read())
                volume_cap = val / 100
                return val
    except:
        pass
    return 10

CoInitialize()

def check_single_instance():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(('127.0.0.1', PORT))
        sock.listen(1)
        threading.Thread(target=ipc_listener, args=(sock,), daemon=True).start()
    except socket.error:
        try:
            s = socket.create_connection(('127.0.0.1', PORT), timeout=1)
            s.sendall(pickle.dumps('SHOW'))
            s.close()
        except:
            pass
        sys.exit()

def ipc_listener(sock):
    while True:
        conn, _ = sock.accept()
        data = b""
        while True:
            part = conn.recv(1024)
            if not part:
                break
            data += part
        try:
            msg = pickle.loads(data)
            if msg == 'SHOW':
                show_window()
        except:
            pass
        conn.close()

check_single_instance()

def get_default_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return cast(interface, POINTER(IAudioEndpointVolume)), devices.GetId()

volume, last_device_id = get_default_volume_interface()

def set_volume(vol):
    global volume
    try:
        volume.SetMasterVolumeLevelScalar(vol, None)
    except:
        pass

def get_volume():
    global volume
    try:
        return volume.GetMasterVolumeLevelScalar()
    except:
        return None

def lock_volume():
    global volume_cap, running, volume, last_device_id
    while running:
        try:
            devices = AudioUtilities.GetSpeakers()
            current_device_id = devices.GetId()
            if current_device_id != last_device_id:
                interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                last_device_id = current_device_id
            current_volume = get_volume()
            if current_volume is not None and current_volume > volume_cap:
                set_volume(volume_cap)
        except:
            pass
        time.sleep(0.1)

def on_slider_change(val):
    global volume_cap
    volume_cap = float(val) / 100
    save_settings()
    try:
        current_volume = get_volume()
        if current_volume is not None and current_volume > volume_cap:
            set_volume(volume_cap)
    except:
        pass

def create_gui():
    global root, slider
    root = tk.Tk()
    root.withdraw()

    root.title("Volume Cap")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", hide_window)
    root.attributes("-topmost", True)

    root.update_idletasks()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 110
    x_margin = 40
    y_margin = 100

    x = screen_width - window_width - x_margin
    y = screen_height - window_height - y_margin

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label = tk.Label(root, text="Set Volume Cap (%)")
    label.pack(pady=5)

    slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=on_slider_change, length=150)
    slider.set(load_settings())
    slider.pack()

    root.mainloop()

def hide_window():
    root.withdraw()

def show_window():
    if root:
        root.deiconify()
        root.lift()
        root.after(0, root.focus_force)

threading.Thread(target=create_gui, daemon=True).start()
lock_volume()
