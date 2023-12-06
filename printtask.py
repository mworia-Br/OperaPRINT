import psutil

def end_task(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            pid = process.info['pid']
            psutil.Process(pid).terminate()
            print(f"Successfully ended {process_name} (PID: {pid})")

# Example: end the task for Notepad
end_task("msedge.exe")
