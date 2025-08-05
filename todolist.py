import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                task_list.insert(tk.END, line.strip())

def save_tasks():
    tasks = task_list.get(0, tk.END)
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_complete():
    try:
        index = task_list.curselection()[0]
        task = task_list.get(index)
        if not task.startswith("[✓]"):
            task_list.delete(index)
            task_list.insert(index, "[✓] " + task)
            save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

# GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

tk.Label(root, text="To-Do List", font=("Helvetica", 16)).pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)

task_list = tk.Listbox(root, width=40, height=10)
task_list.pack(pady=10)

tk.Button(root, text="Remove Task", command=delete_task).pack(pady=5)
tk.Button(root, text="Mark as Complete", command=mark_complete).pack(pady=5)

# Load saved tasks on start
load_tasks()

root.mainloop()