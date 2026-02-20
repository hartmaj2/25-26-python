# Tkinter notes

- the main window is a `Tk()` object

- when creating a widget - set `master` to set the parent widget

## Tk important functions

- `mainloop()` - rozběhne hlavní smyčku (smyčka čeká na události od uživatele)

- `pack()` - spočítá, kde se má již nakonfigurovaný widget objevit a ukáže ho

- `config()` - upraví stav widgetu za běhu programu 

## Other functions

- `geometry("WxH+X+Y")` - nastaví pozici hlavního okna na obrazovce

- `focus_force()` - zasoustředí OS na toto okno (klávesnice atd.)

## Button

### Attributes

- text
- command