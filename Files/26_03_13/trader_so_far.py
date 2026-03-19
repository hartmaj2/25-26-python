import tkinter as tk
from tkinter import ttk
import random


root = tk.Tk()

# STATS
money = 100
j_price = random.randint(10,30)
j_count = 0

b_price = random.randint(10,30)
b_count = 0

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
    global j_count,money
    j_count += 1
    money -= j_price


def sell_apples():
    ...

j_frame = tk.Frame(master=red_frame)
j_frame.pack()

j_price_label = tk.Label(master=j_frame,text=f"Jablka cena: {j_price}")
j_price_label.pack(side="left")

j_count_label = tk.Label(master=j_frame,text=f"Počet: {j_count}")
j_count_label.pack(side="left")

j_buy_button = ttk.Button(master=j_frame,text="Buy",command=buy_apples)
j_buy_button.pack(side="left")

j_sell_button = ttk.Button(master=j_frame,text="Sell",command=sell_apples)
j_sell_button.pack(side="left")

## banany
b_frame = tk.Frame(master=red_frame)
b_frame.pack()

b_price_label = tk.Label(master=b_frame,text=f"Banany cena: {b_price}")
b_price_label.pack(side="left")

b_count_label = tk.Label(master=b_frame,text=f"Počet: {b_count}")
b_count_label.pack(side="left")

b_buy_button = ttk.Button(master=b_frame,text="Buy")
b_buy_button.pack(side="left")

b_sell_button = ttk.Button(master=b_frame,text="Sell")
b_sell_button.pack(side="left")

root.mainloop()