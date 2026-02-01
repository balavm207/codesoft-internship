import tkinter as tk
from tkinter import messagebox
from datetime import date

# Main window
app = tk.Tk()
app.title("Personal To-Do Manager")
app.geometry("420x500")
app.resizable(False, False)

task_list = []

# ---------- Functions ----------

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    task_list.append(task)
                    task_box.insert(tk.END, task)
    except:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in task_list:
            file.write(task + "\n")

def add_task():
    task = entry_task.get()
    if task == "":
        messagebox.showwarning("Input Error", "Task cannot be empty")
    else:
        task_list.append(task)
        task_box.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        index = task_box.curselection()[0]
        task_box.delete(index)
        task_list.pop(index)
        save_tasks()
    except:
        messagebox.showwarning("Selection Error", "Please select a task")

def mark_done():
    try:
        index = task_box.curselection()[0]
        task = task_box.get(index)
        task_box.delete(index)
        task_box.insert(index, f"✔ {task}")
    except:
        messagebox.showwarning("Selection Error", "Please select a task")

def clear_all():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        task_box.delete(0, tk.END)
        task_list.clear()
        save_tasks()

# ---------- UI ----------

title = tk.Label(app, text="My To-Do List", font=("Arial", 20, "bold"))
title.pack(pady=10)

today = tk.Label(app, text=f"Date: {date.today()}", font=("Arial", 10))
today.pack()

entry_task = tk.Entry(app, font=("Arial", 14), width=28)
entry_task.pack(pady=12)

btn_add = tk.Button(app, text="Add Task", width=22, command=add_task)
btn_add.pack(pady=4)

btn_done = tk.Button(app, text="Mark as Done", width=22, command=mark_done)
btn_done.pack(pady=4)

btn_delete = tk.Button(app, text="Delete Task", width=22, command=delete_task)
btn_delete.pack(pady=4)

btn_clear = tk.Button(app, text="Clear All Tasks", width=22, command=clear_all)
btn_clear.pack(pady=6)

task_box = tk.Listbox(app, font=("Arial", 12), width=38, height=10)
task_box.pack(pady=15)

load_tasks()

app.mainloop()
