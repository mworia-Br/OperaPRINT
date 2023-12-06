import tkinter as tk
from tkinter import messagebox
import psutil

def end_tasks(process_names):
    terminated_pids = []
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] in process_names:
            pid = process.info['pid']
            psutil.Process(pid).terminate()
            terminated_pids.append(pid)

    if terminated_pids:
        # Construct the success message with the list of terminated PIDs
        success_message = f"Successfully ended {', '.join(process_names)} processes (PIDs: {', '.join(map(str, terminated_pids))})"
        print(success_message)
        return success_message
    else:
        return f"No processes found with the names {', '.join(process_names)}"

def on_button_click():
    chrome_process_name = "chrome.exe"
    edge_process_name = "msedge.exe"

    result_chrome = end_tasks([chrome_process_name])
    result_edge = end_tasks([edge_process_name])

    result = result_chrome + "\n" + result_edge
    messagebox.showinfo("Task Ended", result)

# Create the main application window
app = tk.Tk()
app.title("IT Auto App")

# Create a label for the landing page description
label_description = tk.Label(app, text="Self-service app for print issues while using msedge and google chrome. \nThis program will automatically close all specified tasks.")
label_description.pack(pady=10)

# Create a button to trigger the end_tasks function
button_end_task = tk.Button(app, text="End Tasks", command=on_button_click)
button_end_task.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
