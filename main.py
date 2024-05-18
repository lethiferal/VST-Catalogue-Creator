import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


def search():
    vst3 = entry1.get()
    vst2 = entry2.get()
    vsts = []

    for root, dirs, files in os.walk(vst3):
        for file in files:
            if file.endswith(".vst3"):
                name = (
                    os.path.splitext(file)[0]
                    .replace("_", " ")
                    .replace("x64", "64-bit")
                    .replace("x86", "32-bit")
                )
                if name not in vsts:
                    vsts.append(name)

    for root, dirs, files in os.walk(vst2):
        for file in files:
            if file.endswith(".dll"):
                name = (
                    os.path.splitext(file)[0]
                    .replace("_", " ")
                    .replace("x64", "64-bit")
                    .replace("x86", "32-bit")
                )
                if name not in vsts:
                    vsts.append(name)

    vsts.sort()

    text.delete(1.0, tk.END)
    for vst in vsts:
        text.insert(tk.END, vst + "\n")
    button.config(text="Refresh")


def browse1():
    folder_path = filedialog.askdirectory()
    entry1.delete(0, tk.END)
    entry1.insert(0, folder_path)


def browse2():
    folder_path = filedialog.askdirectory()
    entry2.delete(0, tk.END)
    entry2.insert(0, folder_path)


default1 = "C:/Program Files/Common Files/VST3"
default2 = "C:/Program Files/Common Files/VST2"

root = tk.Tk()
root.title("VST Catalogue Creator")

root.wm_attributes("-toolwindow", True)

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

label1 = ttk.Label(frame, text="VST3 Folder:")
label1.grid(row=0, column=0, sticky="w")

entry1 = ttk.Entry(frame, width=50)
entry1.grid(row=0, column=1, padx=5, pady=5)
entry1.insert(0, default1)

button1 = ttk.Button(frame, text="Browse", command=browse1)
button1.grid(row=0, column=2, padx=5, pady=5)

label2 = ttk.Label(frame, text="VST2 Folder:")
label2.grid(row=1, column=0, sticky="w")

entry2 = ttk.Entry(frame, width=50)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.insert(0, default2)

button2 = ttk.Button(frame, text="Browse", command=browse2)
button2.grid(row=1, column=2, padx=5, pady=5)

button = ttk.Button(frame, text="Search Plugins", command=search)
button.grid(row=2, columnspan=3, pady=10)

scrollbar = tk.Scrollbar(root)

text = tk.Text(root, width=80, height=20, yscrollcommand=scrollbar.set)


def show_list():
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(pady=10)
    scrollbar.config(command=text.yview)
    button.config(text="Refresh")


button.config(command=lambda: [search(), show_list()])

root.mainloop()
