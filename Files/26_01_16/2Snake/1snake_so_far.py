ax = 0
ay = 0

def spawn_apple():
    global ax,ay
    ax = randint(0,4)
    ay = randint(0,4)

px = 2
py = 2

dirc = 1

def draw():
    for i in range(5):
        for j in range(5):
            if i == px and j == py:
                led.plot(i, j)
            elif i == ax and j == ay:
                led.plot_brightness(i, j, 50)
            else:
                led.unplot(i, j)

def move():
    global px,py
    if dirc == 0:
        py -= 1
    if dirc == 1:
        px += 1
    if dirc == 2:
        py += 1
    if dirc == 3:
        px -= 1
    
    if px == 5:
        px = 0
    if px == -1:
        px = 4
    
    if py == 5:
        py = 0
    if py == -1:
        py = 4

def turn_right():
    global dirc
    dirc += 1
    if dirc == 4:
        dirc = 0

def turn_left():
    global dirc
    dirc -= 1
    if dirc == -1:
        dirc = 3
    pass

input.on_button_pressed(Button.A, turn_left)
input.on_button_pressed(Button.B, turn_right)

spawn_apple()
while True:
    draw()
    pause(500)
    move()
    if px == ax and py == ay:
        spawn_apple()
