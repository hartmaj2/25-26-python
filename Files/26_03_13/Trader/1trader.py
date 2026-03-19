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
items = 0
days = 0

# ITEM stats

item_price = 0

# HUD GUI

def udpate_stat_gui():
    money_label.config(text=f"{money_text}{money}")
    items_label.config(text=f"{items_text}{items}")
    days_label.config(text=f"{days_text}{days}")

hud = tk.Frame(root,width=500,height=100,bg="red")
hud.pack(pady=25)

money_label = tk.Label(hud)
money_text = "Money: "
money_label.pack(side="left",padx=25)

items_label = tk.Label(hud)
items_text = "Items: "
items_label.pack(side="left",padx=25)

days_label = tk.Label(hud)
days_text = "Days: "
days_label.pack(side="left",padx=25)

udpate_stat_gui()

# SHOP GUI

def buy_action():
    global money, items
    if money >= item_price:
        money -= item_price
        items += 1

    udpate_stat_gui()

def sell_action():
    global money, items
    if items >= 1:
        money += item_price
        items -= 1

    udpate_stat_gui()

def update_shop_gui():
    price_label.config(text=f"{price_text}{item_price}")

shop = tk.Frame(root,width=500,height=500,bg="green")
shop.pack(pady=25)

price_label = tk.Label(shop)
price_text = "🍎 price: "
price_label.pack(side="left")

buy_button = ttk.Button(shop,text="Buy",command=buy_action)
buy_button.pack(side="right",padx=25)

sell_button = ttk.Button(shop,text="Sell",command=sell_action)
sell_button.pack(side="left",padx=25)

# NEXT DAY

def new_day():
    global item_price,days
    item_price = random.randint(10,50)
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