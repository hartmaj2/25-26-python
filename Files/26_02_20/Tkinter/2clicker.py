import tkinter

# --- data programu ---

score = 0

# --- nastaveni hlavniho okna ---

okno = tkinter.Tk()

okno.focus_force()

okno.geometry("400x300+500+300")

# --- ukazatel skore ---

label = tkinter.Label(master=okno)
label.config(text=score)
label.pack()

# --- tlacitko ---

def klikni():
    global score
    score += 1
    label.config(text=score)

tlacitko = tkinter.Button(master=okno,text="Click me",command=klikni)
tlacitko.pack()

okno.mainloop()