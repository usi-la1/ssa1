import requests
import subprocess
import os
import time
import tkinter as tk
from tkinter import ttk

APP_PATH = "app.py"
VERSION_URL = "https://raw.githubusercontent.com/USERNAME/REPO/main/version.txt"
APP_URL = "https://raw.githubusercontent.com/USERNAME/REPO/main/app.py"

CURRENT_VERSION = "1.0"

def update_and_run():
    status.set("جاري التحقق من التحديث...")
    progress["value"] = 20
    root.update()

    try:
        online_version = requests.get(VERSION_URL).text.strip()

        if online_version != CURRENT_VERSION:
            status.set("يوجد تحديث، جاري التحميل...")
            progress["value"] = 50
            root.update()

            new_app = requests.get(APP_URL).text
            with open(APP_PATH, "w", encoding="utf-8") as f:
                f.write(new_app)

            progress["value"] = 90
            status.set("تم التحديث")

        else:
            status.set("لا يوجد تحديث")

    except:
        status.set("فشل الاتصال")

    progress["value"] = 100
    root.update()
    time.sleep(1)

    subprocess.Popen(["python", APP_PATH])
    root.destroy()

# -------- واجهة --------
root = tk.Tk()
root.title("Updater")
root.geometry("300x180")

tk.Button(root, text="ابدأ", command=update_and_run).pack(pady=10)

progress = ttk.Progressbar(root, length=200)
progress.pack(pady=5)

status = tk.StringVar()
tk.Label(root, textvariable=status).pack()

tk.Label(root, text=f"Launcher v{CURRENT_VERSION}", fg="gray").place(x=5, y=155)

root.mainloop()
