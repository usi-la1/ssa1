import tkinter as tk

root = tk.Tk()
root.title("My App")
root.geometry("300x200")

tk.Label(root, text="التطبيق يعمل ✅", font=("Arial", 14)).pack(expand=True)

root.mainloop()
