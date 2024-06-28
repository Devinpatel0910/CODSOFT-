import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("800x600")

        # Create a frame for the to-do list
        self.list_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.list_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Create a label and entry for the task
        tk.Label(self.list_frame, text='TO-DO LIST', font=('Cambria', 34, "bold"), bg='#f0f0f0', fg='#535798').pack(pady=20)
        self.task_label = tk.Label(self.list_frame, text="Task:", font=('Cambria', 14), bg='#f0f0f0')
        self.task_label.pack()
        self.task_entry = tk.Entry(self.list_frame, width=30, font=('Cambria', 14))
        self.task_entry.pack(pady=10)
        # Create buttons
        button_frame = tk.Frame(self.list_frame, bg='#f0f0f0')
        button_frame.pack(pady=20)
        self.add_button = tk.Button(button_frame, text="Add Task", font=('Comic Sans MS', 12, "bold"), bg='lavender', fg='#535798', command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10)
        self.delete_button = tk.Button(button_frame, text="Delete Task", font=('Comic Sans MS', 12, "bold"), bg='lavender', fg='#535798', command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)
        self.edit_button = tk.Button(button_frame, text="Edit Task", font=('Comic Sans MS', 12, "bold"), bg='lavender', fg='#535798', command=self.edit_task)
        self.edit_button.pack(side=tk.LEFT, padx=10)
        self.view_button = tk.Button(button_frame, text="View Tasks", font=('Comic Sans MS', 12, "bold"), bg='lavender', fg='#535798', command=self.view_tasks)
        self.view_button.pack(side=tk.LEFT, padx=10)

        # Create a listbox to display tasks
        self.task_list = tk.Listbox(self.list_frame, width=40, height=10, font=('Comic Sans MS', 12))
        self.task_list.pack(pady=20)

        # Create a variable to store the selected task
        self.selected_task = None

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
        except:
            messagebox.showerror("Error", "Select a task to delete")

    def edit_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.selected_task = self.task_list.get(task_index)
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, self.selected_task)
        except:
            messagebox.showerror("Error", "Select a task to edit")

    def view_tasks(self):
        tasks = self.task_list.get(0, tk.END)
        messagebox.showinfo("Tasks", "\n".join(tasks))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    app.run()