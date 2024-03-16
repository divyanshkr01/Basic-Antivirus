import tkinter as tk
from tkinter import filedialog
import hashlib
import os
import shutil

# Step 1: Ask for the target directory through a GUI
root = tk.Tk()
root.withdraw()
target_directory = filedialog.askdirectory(title="Select Target Directory")

# Step 2: Calculate MD5 hashes of all files in the directory
file_hashes = []
for root_dir, _, filenames in os.walk(target_directory):
    for filename in filenames:
        file_path = os.path.join(root_dir, filename)
        with open(file_path, 'rb') as file:
            file_data = file.read()
            md5_hash = hashlib.md5(file_data).hexdigest()
            file_hashes.append((filename, md5_hash))

# Step 3: Compare calculated hashes with the dataset
with open(r'D:\Education\B. Tech\Project\Minor\6th Sem\Minor-2\Anti-Virus\END-SEM\FINAL\Anti-Virus\Spook\Anti-Virus\Hashes.txt', 'r') as dataset_file:
    dataset_hashes = [line.strip() for line in dataset_file]

found_malware = False
malware_files = []

for file_name, file_hash in file_hashes:
    if file_hash in dataset_hashes:
        found_malware = True
        malware_files.append(file_name)
        print(f"Malware found: {file_name} is found to be a Malware from our Database.")

# Step 4: Process user's choice
if not found_malware:
    print("No malware found.")
else:
    choice = input("Do you want to Quarantine the File? [LEAVE/CAPTURE] ").lower()
    if choice == 'leave':
        print("You are in danger!")
        exit()
    elif choice == 'capture':
        quarantine_folder = os.path.join(target_directory, 'Quarantined Files')
        os.makedirs(quarantine_folder, exist_ok=True)
        for file_name in malware_files:
            file_path = os.path.join(target_directory, file_name)
            shutil.move(file_path, quarantine_folder)
        print("Files moved to Quarantined Files folder.")

        # Step 5: Freeze the 'Quarantined Files' folder
        os.chmod(quarantine_folder, 0o444)
        freeze_file = os.path.join(quarantine_folder, '.freeze')
        with open(freeze_file, 'w') as freeze:
            pass

        choice = input("Do you want to delete the Malware(s)? [MERCY/EXECUTE] ").lower()
        if choice == 'mercy':
            print("You are still in danger!")
            exit()
        elif choice == 'execute':
            shutil.rmtree(quarantine_folder)
            print("Malware has been executed, you are safe now!")
        else:
            print("Invalid choice. Exiting.")
            exit()
