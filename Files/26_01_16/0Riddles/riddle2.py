# Riddle 2 - what will we see after I press the button

x = 0

while True:
    led.plot(x,2)
    if input.button_is_pressed(Button.A):
        x += 1