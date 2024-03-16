import psutil
import os
import signal

def get_running_processes():
    process_list = []

    try:
        for proc in psutil.process_iter(['pid', 'name']):
            process_list.append((proc.info['pid'], proc.info['name']))
        
        return process_list
    
    except psutil.Error as e:
        print(f"Error occurred while retrieving running processes: {e}")
        return []

def kill_process_by_pid(pid):
    try:
        # Send SIGTERM signal to the process
        os.kill(int(pid), signal.SIGTERM)
        print(f"Process with PID {pid} killed.")
    
    except OSError as e:
        print(f"Error occurred while trying to kill process with PID {pid}: {e}")

def main():
    processes = get_running_processes()

    print("Running processes:")
    for pid, name in processes:
        print(f"PID: {pid}\tName: {name}")

    choice = input("Do you want to kill a process? (yes/no): ")

    if choice.lower() == 'yes':
        pid = input("Enter the PID of the process you want to kill: ")
        kill_process_by_pid(pid)
    else:
        print("No process will be killed.")

if __name__ == "__main__":
    main()
