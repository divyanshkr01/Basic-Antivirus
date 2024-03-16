import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import shutil
import os

def select_directory():
    target_dir = filedialog.askdirectory()
    backup_directory(target_dir)

def backup_directory(target_dir):
    backup_dir1 = r'D:\Education\B. Tech\Project\Minor\6th Sem\Minor-2\Anti-Virus\END-SEM\FINAL\Anti-Virus\Spook\Anti-Virus\Back-Up'
    backup_dir2 = r'C:\Users\ameyk\OneDrive - UPES\MINOR\Modules\Back-Up'
    backup_name = 'Back-Up'

    if not os.path.exists(backup_dir1):
        os.makedirs(backup_dir1)

    if not os.path.exists(backup_dir2):
        os.makedirs(backup_dir2)

    backup_path1 = os.path.join(backup_dir1, backup_name)
    backup_path2 = os.path.join(backup_dir2, backup_name)

    try:
        shutil.make_archive(backup_path1, 'zip', target_dir)
        shutil.make_archive(backup_path2, 'zip', target_dir)
        result_label.config(text=f"Backups created successfully at {backup_path1} and {backup_path2}", foreground="green")
    except Exception as e:
        result_label.config(text=f"Error creating backups: {str(e)}", foreground="red")

window = tk.Tk()
window.title("Backup Creator")

frame = ttk.Frame(window, padding="20")
frame.pack()

label = ttk.Label(frame, text="Select the target directory:")
label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

select_button = ttk.Button(frame, text="Select Directory", command=select_directory)
select_button.grid(row=1, column=0, padx=(0, 10))

result_label = ttk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2)

window.mainloop()
