# Co bude dělat čudlík po kliknutí na něj?

import tkinter as tk
from tkinter import ttk

money = 10

def add_money():
    global money
    money += 1

root = tk.Tk()

label = ttk.Label(master=root,text=f"Money: {money}")
label.pack()

button = ttk.Button(master=root,text="Earn money",command=add_money)
button.pack()

root.mainloop()