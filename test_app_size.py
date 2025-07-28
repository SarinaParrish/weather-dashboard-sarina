import tkinter as tk

root = tk.Tk()
root.geometry("400x600")
root.resizable(False, False)

tk.Label(root, text="HELLO FROM THE BASELINE", font=("Arial", 16)).pack(pady=250)

root.mainloop()
