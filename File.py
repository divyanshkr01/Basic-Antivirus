import tkinter as tk
from tkinter import filedialog
import hashlib
import os
import subprocess

def calculate_md5(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        md5_hash = hashlib.md5(file_data).hexdigest()
        return md5_hash

def scan_file(file_path, dataset_file_path):
    file_hash = calculate_md5(file_path)
    with open(dataset_file_path, 'r') as dataset_file:
        dataset_hashes = [line.strip() for line in dataset_file]
    if file_hash in dataset_hashes:
        print(f"Malware found: {file_path} is found to be a Malware from our Database.")
        choice = input("Do you want to search the whole directory? [Y/N] ").upper()
        if choice == 'Y':
            run_main_script()
    else:
        print("No malware found.")

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select File")
    return file_path

def run_main_script():
    main_script_path = r'D:\Education\B. Tech\Project\Minor\6th Sem\Minor-2\Anti-Virus\END-SEM\FINAL\Anti-Virus\Spook\Anti-Virus\StreamLine\Main.py'  # Specify the path to Main.py
    subprocess.call(["python", main_script_path])

# Example usage
def main():
    file_path = select_file()
    dataset_file_path = r'D:\Education\B. Tech\Project\Minor\6th Sem\Minor-2\Anti-Virus\END-SEM\FINAL\Anti-Virus\Spook\Anti-Virus\Hashes.txt'
    if file_path:
        scan_file(file_path, dataset_file_path)


if __name__ == '__main__':
    main()
