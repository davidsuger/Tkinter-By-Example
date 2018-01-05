import tkinter as tk
from tkinter import ttk


class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        self.tasks = []

        self.title('To Do App v1')
        self.geometry('300x400+800+300')

        self.color_schemes = [{'background': 'lightblue', 'foreground': 'black'},
                              {'background': 'lightgreen', 'foreground': 'white'}]

        task0 = ttk.Label(self, text='Add task below', background='lightblue', foreground='black', anchor='center',
                          font=('Arial', 14, 'bold'))
        self.tasks.append(task0)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X, pady=1)

        self.textInput = tk.Text(self, height=3)
        self.textInput.pack(side=tk.BOTTOM)
        self.textInput.focus_set()

        self.bind('<Return>', self.addTask)
        #  这样加不行
        # self.textInput.bind('<Return>', self.addTask)

    def addTask(self, event):
        self.textInput.mark_set('insert', '1.0')
        task_text = self.textInput.get('1.0', 'end').strip()
        if len(task_text) > 0:
            color_schemes_index = len(self.tasks) % 2
            task = ttk.Label(self, text=task_text,
                             background=self.color_schemes[color_schemes_index]['background'],
                             foreground=self.color_schemes[color_schemes_index]['foreground'], anchor='center',
                             font=('Arial', 14, 'bold'))
            task.pack(side=tk.TOP, fill=tk.X, pady=1)
            self.tasks.append(task)

        self.textInput.delete(1.0, tk.END)


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
