import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import shutil
import os

def select_directory():
    target_dir = filedialog.askdirectory()
    backup_directory(target_dir)

def backup_directory(target_dir):
    backup_dir = r'D:\Education\B. Tech\Project\Minor\6th Sem\Minor-2\Anti-Virus\END-SEM\FINAL\Anti-Virus\Spook\Anti-Virus\Back-Up'
    backup_name = 'Backup-File'

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_path = os.path.join(backup_dir, backup_name)

    try:
        shutil.make_archive(backup_path, 'zip', target_dir)
        result_label.config(text=f"Backup created successfully at {backup_path}", foreground="green")
    except Exception as e:
        result_label.config(text=f"Error creating backup: {str(e)}", foreground="red")

window = tk.Tk()
window.title("Backup Creator")

frame = ttk.Frame(window, padding="20")
frame.pack()

label = ttk.Label(frame, text="Select the target directory:")
label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

select_button = ttk.Button(frame, text="Select Directory", command=select_directory)
select_button.grid(row=1, column=0, padx=(0, 10))

result_label = ttk.Label(frame, text="")
result_label.grid(row=1, column=1)

window.mainloop()
