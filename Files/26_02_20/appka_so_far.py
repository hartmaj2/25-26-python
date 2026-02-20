import tkinter

score = 0

def kliknuti():
    global score
    score += 1
    novy = "Score: " + str(score)
    pocitadlo.config(text=novy)
    print(score)

okno = tkinter.Tk() # vytvor objekt okna

okno.title("Moje krásné okénko") # nastavi titulek okna

okno.focus_force() # dej okno do popredi 
okno.geometry("400x300+400+300") # nastavi rozmery okna

pocitadlo = tkinter.Label(text="Score: 0")
pocitadlo.pack()

cudlik = tkinter.Button(text="Klikni si",command=kliknuti) # vytvor cudlik s textem "Klikni si"
cudlik.pack() # vykresli ho

okno.mainloop() # zapni hlavni smycku programu, aby ihned nezkoncil

