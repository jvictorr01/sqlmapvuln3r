import os
import subprocess
import tkinter as tk
from tkinter import ttk

def start_scan():
    url = entry_url.get()
    if url:
        command = f"sqlmap -u {url}"
        subprocess.Popen(["osascript", "-e", f'tell app "Terminal" to do script "{command}"'])
    else:
        status_label.config(text="Por favor, insira uma URL válida")

app = tk.Tk()
app.title("SQLMap SCAN")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_url = ttk.Label(frame, text="URL:")
label_url.grid(row=0, column=0, sticky=(tk.W, tk.E))

entry_url = ttk.Entry(frame, width=50)
entry_url.grid(row=0, column=1, sticky=(tk.W, tk.E))

button_start = ttk.Button(frame, text="Iniciar", command=start_scan)
button_start.grid(row=1, column=0, columnspan=2, pady=10)

status_label = ttk.Label(frame, text="")
status_label.grid(row=2, column=0, columnspan=2)

app.mainloop()
