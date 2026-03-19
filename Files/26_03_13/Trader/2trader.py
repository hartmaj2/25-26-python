# this game will be made in tkinter
# it is a trading game -> in each round we can either sell or buy items for money that we have

import tkinter as tk
from tkinter import ttk
import random

# TODO: create a program with money, and single item, user will be able to click sell or buy the product for given price

root = tk.Tk()

# Center the root window and set its size to 400x500
root.geometry("400x500")
root.eval('tk::PlaceWindow . center')

# STATS

money = 100
days = 0

# ITEM stats

items = {
    f"{"🍎 Apple":10}": {"price": 0, "quantity": 0},
    f"{"🍌 Banana":9}": {"price": 0, "quantity": 0},
    f"{"🍇 Grape":10}": {"price": 0, "quantity": 0}
}

item_labels = {}
price_labels = {}

# HUD GUI

def udpate_stat_gui():
    global item_labels
    money_label.config(text=f"{money_text}{money}")
    days_label.config(text=f"{days_text}{days}")
    
    for item_name, item_data in items.items():
        item_labels[item_name].config(text=f"{item_name}: {item_data['quantity']}")

hud = tk.Frame(root,width=500,height=100)
hud.pack(pady=25)

money_label = tk.Label(hud)
money_text = "Money: "
money_label.pack(side="left",padx=25)

days_label = tk.Label(hud)
days_text = "Days: "
days_label.pack(side="left",padx=25)

# SHOP GUI

def buy_action(item_name):
    global money
    if money >= items[item_name]["price"]:
        money -= items[item_name]["price"]
        items[item_name]["quantity"] += 1
    udpate_stat_gui()

def sell_action(item_name):
    global money
    if items[item_name]["quantity"] > 0:
        money += items[item_name]["price"]
        items[item_name]["quantity"] -= 1
    udpate_stat_gui()

def update_shop_gui():
    for item_name, item_data in items.items():
        price_labels[item_name].config(text=f"Price: {item_data['price']}")

# Create dynamic item labels and buttons

shop = tk.Frame(root,width=500,height=500)
shop.pack(pady=25)

for item_name in items:
    frame = tk.Frame(shop)
    frame.pack(pady=5, fill="x")

    item_labels[item_name] = tk.Label(frame)
    item_labels[item_name].pack(side="left", padx=10)

    price_labels[item_name] = tk.Label(frame)
    price_labels[item_name].pack(side="left", padx=10)

    buy_button = ttk.Button(frame, text="Buy", command=lambda name=item_name: buy_action(name))
    buy_button.pack(side="right", padx=5)

    sell_button = ttk.Button(frame, text="Sell", command=lambda name=item_name: sell_action(name))
    sell_button.pack(side="right", padx=5)

# NEXT DAY

def new_day():
    global days
    for item_name in items:
        items[item_name]["price"] = random.randint(10, 50)
    days += 1
    update_shop_gui()
    udpate_stat_gui()

next_day_button = ttk.Button(root,text="Next day",command=new_day)
next_day_button.pack(pady=50)

# PROGRAM

new_day()
udpate_stat_gui()
update_shop_gui()

# root.focus_force()
root.mainloop()

# TODO: add more items