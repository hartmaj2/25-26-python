import tkinter as tk
from tkinter import ttk
import random


root = tk.Tk()

# STATS
money = 100

a_price = random.randint(10,30)
a_count = 0

b_price = random.randint(10,30)
b_count = 0

# GREEN FRAME

green_frame = tk.Frame(master=root,width=500,height=50,bg="green")
green_frame.pack(side="top")
green_frame.pack_propagate(False) 

label_money = tk.Label(master=green_frame)
label_money.pack(pady=10)

# RED FRAME

red_frame = tk.Frame(master=root,width=500,height=400,bg="red")
red_frame.pack(side="top")

def update_gui():
    label_money.configure(text=f"Money: {money}")

    a_price_label.configure(text=f"Jablka cena: {a_price}")
    a_count_label.configure(text=f"Počet: {a_count}")

    b_price_label.configure(text=f"Banany cena: {b_price}")
    b_count_label.configure(text=f"Počet: {b_count}")

## jablka

def buy_apples():
    global a_count,money
    a_count += 1
    money -= a_price
    update_gui()


def sell_apples():
    ...

a_frame = tk.Frame(master=red_frame)
a_frame.pack()

a_price_label = tk.Label(master=a_frame)
a_price_label.pack(side="left")

a_count_label = tk.Label(master=a_frame)
a_count_label.pack(side="left")

a_buy_button = ttk.Button(master=a_frame,text="Buy",command=buy_apples)
a_buy_button.pack(side="left")

a_sell_button = ttk.Button(master=a_frame,text="Sell",command=sell_apples)
a_sell_button.pack(side="left")

## banany
b_frame = tk.Frame(master=red_frame)
b_frame.pack()

b_price_label = tk.Label(master=b_frame)
b_price_label.pack(side="left")

b_count_label = tk.Label(master=b_frame)
b_count_label.pack(side="left")

b_buy_button = ttk.Button(master=b_frame,text="Buy")
b_buy_button.pack(side="left")

b_sell_button = ttk.Button(master=b_frame,text="Sell")
b_sell_button.pack(side="left")

update_gui()
root.mainloop()