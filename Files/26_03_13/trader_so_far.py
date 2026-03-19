import tkinter as tk
from tkinter import ttk
import random


root = tk.Tk()

# STATS
money = 100
price_j = random.randint(10,30)
price_b = random.randint(10,30)
count_j = 0
count_b = 0

# GREEN FRAME

green_frame = tk.Frame(master=root,width=500,height=50,bg="green")
green_frame.pack(side="top")
green_frame.pack_propagate(False) 

label_money = tk.Label(master=green_frame,text=f"Money: {money}")
label_money.pack(pady=10)

# RED FRAME

red_frame = tk.Frame(master=root,width=500,height=400,bg="red")
red_frame.pack(side="top")

## jablka

def buy_apples():
    global count_j,money
    count_j += 1
    money -= price_j


def sell_apples():
    ...

j_frame = tk.Frame(master=red_frame)
j_frame.pack()

price_jl = tk.Label(master=j_frame,text=f"Jablka cena: {price_j}")
price_jl.pack(side="left")

count_jl = tk.Label(master=j_frame,text=f"Počet: {count_j}")
count_jl.pack(side="left")

button_jb = ttk.Button(master=j_frame,text="Buy",command=buy_apples)
button_jb.pack(side="left")

button_js = ttk.Button(master=j_frame,text="Sell",command=sell_apples)
button_js.pack(side="left")

## banany
b_frame = tk.Frame(master=red_frame)
b_frame.pack()

price_bl = tk.Label(master=b_frame,text=f"Banany cena: {price_b}")
price_bl.pack(side="left")

count_bl = tk.Label(master=b_frame,text=f"Počet: {count_b}")
count_bl.pack(side="left")

button_bb = ttk.Button(master=b_frame,text="Buy")
button_bb.pack(side="left")

button_bs = ttk.Button(master=b_frame,text="Sell")
button_bs.pack(side="left")

root.mainloop()