import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def delete_task(self, task):
        self.tasks.remove(task)
        
    def complete_task(self, task):
        task.completed = True
        
    def get_tasks(self):
        return self.tasks


class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False


class TaskManagerApp(tk.Tk):
    def __init__(self, task_manager):
        super().__init__()
        self.task_manager = task_manager
        self.title("Task Manager")
        self.configure(bg="#FCE4EC")  # Color de fondo rosado claro
        self.geometry("400x500")  # Tamaño de la ventana
        
        self.task_frame = tk.Frame(self, bg="#FCE4EC")
        self.task_frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.task_frame, bg="#E3F2FD", fg="#000000", selectbackground="#90CAF9", selectforeground="#FFFFFF")
        self.task_listbox.pack()
        
        self.refresh_tasks()
        
        self.task_entry = tk.Entry(self, bg="#FFFFFF")
        self.task_entry.pack(pady=5)
        
        self.add_button = tk.Button(self, text="Agregar Tarea", command=self.add_task, bg="#FFCDD2", fg="#000000", activebackground="#F06292", activeforeground="#FFFFFF")
        self.add_button.pack(pady=5)
        
        self.delete_button = tk.Button(self, text="Eliminar Tarea", command=self.delete_task, bg="#FFCDD2", fg="#000000", activebackground="#F06292", activeforeground="#FFFFFF")
        self.delete_button.pack(pady=5)
        
        self.complete_button = tk.Button(self, text="Completar Tarea", command=self.complete_task, bg="#FFCDD2", fg="#000000", activebackground="#F06292", activeforeground="#FFFFFF")
        self.complete_button.pack(pady=5)
        
    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        tasks = self.task_manager.get_tasks()
        for task in tasks:
            status = "Completada" if task.completed else "Pendiente"
            self.task_listbox.insert(tk.END, f"{task.name} - {status}")
            
    def add_task(self):
        task_name = self.task_entry.get()
        if task_name:
            task = Task(task_name)
            self.task_manager.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks()
            
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.task_manager.get_tasks()[selected_index[0]]
            self.task_manager.delete_task(task)
            self.refresh_tasks()
            
    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.task_manager.get_tasks()[selected_index[0]]
            self.task_manager.complete_task(task)
            self.refresh_tasks()


if __name__ == "__main__":
    task_manager = TaskManager()
    app = TaskManagerApp(task_manager)
    app.mainloop()
