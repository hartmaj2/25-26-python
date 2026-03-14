import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

# should be a simulation of knapsack problem in tkinter
# the items are loaded from json file and then player can select some items to take or not
# the selection is done using a grid of canvas rectangles which are clickable and each represents some item
# the rectangles should have visible weight, value and item id

# above the grid should be a frame with panel showing capacity, current total value and current total weight 

class Item:
    
    def __init__(self, id, value, weight):
        self.id = id
        self.value = value
        self.weight = weight


class ItemCanvas:
    def __init__(self, master, item, x, y, width, height, on_select):
        self.master = master
        self.item = item
        self.selected = False
        self.on_select = on_select
        self.rect = master.create_rectangle(
            x, y, x + width, y + height,
            fill="white", outline="black", width=2
        )
        self.text = master.create_text(
            x + width // 2, y + height // 2,
            text=f"⚖️: {item.weight}\n\n💰: {item.value}",
            font=("Arial", 15),
            fill="black"
        )
        master.tag_bind(self.rect, "<Button-1>", self.toggle)
        master.tag_bind(self.text, "<Button-1>", self.toggle)

    def toggle(self, event):
        self.selected = not self.selected
        color = "lightgreen" if self.selected else "white"
        self.master.itemconfig(self.rect, fill=color)
        self.on_select(self)

    def set_selected(self, selected):
        self.selected = selected
        color = "lightgreen" if self.selected else "white"
        self.master.itemconfig(self.rect, fill=color)

BASE_W_TEXT = "Total ⚖️: "
BASE_V_TEXT = "Total 💰: "


class KnapsackApp:
    def __init__(self, root, json_file):
        self.root = root
        self.json_file = json_file
        self.items = []
        self.capacity = 0
        self.total_weight = 0
        self.total_value = 0
        self.item_canvases = []

        self.load_items()
        self.create_ui()

    def load_items(self):
        with open(self.json_file, 'r') as f:
            data = json.load(f)
            self.capacity = data['capacity']
            self.items = [Item(item['id'], item['value'], item['weight']) for item in data['items']]

    def create_ui(self):
        # Top panel
        top_frame = ttk.Frame(self.root)
        top_frame.pack(pady=10)

        self.capacity_label = tk.Label(top_frame, text=f"Max ⚖️: {self.capacity}")
        self.capacity_label.pack(side=tk.LEFT, padx=10)

        self.weight_label = tk.Label(top_frame, text=f"{BASE_W_TEXT}{self.total_weight}")
        self.weight_label.pack(side=tk.LEFT, padx=10)

        self.value_label = tk.Label(top_frame, text=f"{BASE_V_TEXT}{self.total_value}")
        self.value_label.pack(side=tk.LEFT, padx=10)

        # Canvas grid
        canvas_frame = ttk.Frame(self.root)
        canvas_frame.pack()

        self.canvas = tk.Canvas(canvas_frame, width=500, height=500, bg="lightgray")
        self.canvas.pack()

        self.create_item_grid()

        # Frame for submit value button
        records_frame = ttk.Frame(self.root)
        records_frame.pack(pady=10)

        self.submit_button = ttk.Button(records_frame, text="Submit Value", command=self.submit_value)
        self.submit_button.pack()

        self.records_listbox = tk.Listbox(records_frame, height=10, width=30)
        self.records_listbox.pack(pady=5)

    def create_item_grid(self):
        cols = 5
        rows = (len(self.items) + cols - 1) // cols
        width, height = 80, 80
        padding = 10

        for i, item in enumerate(self.items):
            x = (i % cols) * (width + padding) + padding
            y = (i // cols) * (height + padding) + padding
            item_canvas = ItemCanvas(self.canvas, item, x, y, width, height, self.update_selection)
            self.item_canvases.append(item_canvas)

    def update_selection(self, item_canvas):
        self.total_weight = sum(ic.item.weight for ic in self.item_canvases if ic.selected)
        self.total_value = sum(ic.item.value for ic in self.item_canvases if ic.selected)

        self.weight_label.config(text=f"{BASE_W_TEXT}{self.total_weight}")
        self.value_label.config(text=f"{BASE_V_TEXT}{self.total_value}")

        if self.total_weight > self.capacity:
            self.weight_label.config(fg="red")
        else:
            self.weight_label.config(fg="white")

    def submit_value(self):
        if self.total_weight <= self.capacity:
            self.records_listbox.insert(tk.END, f"Value: {self.total_value}")
            # sort the items in the listbox based on value
            items = list(self.records_listbox.get(0, tk.END))
            items.sort(key=lambda x: int(x.split(': ')[1]),reverse=True)
            self.records_listbox.delete(0, tk.END)
            for item in items:
                self.records_listbox.insert(tk.END, item)
        else:
            messagebox.showerror("Error", "Total weight exceeds capacity!")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Knapsack Problem Simulation")
    root.focus_force()
    app = KnapsackApp(root, "Files/26_03_12/Knapsack/knapsack.json")
    root.mainloop()

# From knapsack.json possible to get 247


