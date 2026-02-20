import tkinter

window = tkinter.Tk()

c1 = tkinter.Canvas(window,width=300,height=200,bg="red")
c1.pack(side="left")

c2 = tkinter.Canvas(window,width=300,height=200,bg="green")
c2.pack(side="right")

c3 = tkinter.Canvas(window,width=300,height=200,bg="blue")
c3.pack()

c4 = tkinter.Canvas(window,width=300,height=200,bg="yellow")
c4.pack()

c5 = tkinter.Canvas(window,width=300,height=200,bg="pink")
c5.pack(side="left")

window.mainloop()