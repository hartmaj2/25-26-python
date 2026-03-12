import tkinter as tk
from tkinter import ttk

labels = []

def submit_text():
    weight = entry.get().strip()
    entry.delete(0, tk.END)

    value = entry2.get().strip()
    entry2.delete(0, tk.END)

    canvas = tk.Canvas(frame2, width=150, height=50)
    canvas.pack(pady=5)

    canvas.create_rectangle(5, 5, 145, 45)
    canvas.create_text(75, 25, text=f"W:{weight} V:{value}")

    canvas.bind("<Button-1>", lambda e: print("Clicked", weight, value))

root = tk.Tk()
root.focus_force()

root.title("Nice GUI")

frame = ttk.Frame(root,padding=20)
frame.pack()

frame2 = ttk.Frame(root,padding=20)
frame2.pack()

label = ttk.Label(frame, text="Enter item weight")
label.pack(pady=5)

entry = ttk.Entry(frame)
entry.pack(pady=5)

label2 = ttk.Label(frame, text="Enter item value")
label2.pack(pady=5)

entry2 = ttk.Entry(frame)
entry2.pack(pady=5)
# entry.bind(sequence="<Return>",func=submit_text)

button = ttk.Button(frame, text="Submit", command=submit_text)
button.pack(pady=10)

root.mainloop()