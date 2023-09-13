import tkinter as tk


def add_tasks():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)


# Create the main window
window = tk.Tk()
window.title("To-Do List")
window.geometry("300x300")
window.configure(bg="red")

# Create and configure a listbox to display tasks
listbox = tk.Listbox(window, selectmode=tk.SINGLE)
listbox.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

# Create an entry widget for adding tasks
entry = tk.Entry(window)
entry.pack(pady=5, padx=10, expand=True, fill=tk.BOTH)

# Create buttons for adding and deleting tasks
add_button = tk.Button(window, text="Add a Task", command=add_tasks)
add_button.pack(pady=5)
delete_button = tk.Button(window, text="Remove a Task", command=remove_task)
delete_button.pack(pady=5)

# Run the Tkinter main loop
window.mainloop()
