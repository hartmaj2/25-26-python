# Snake without apples and without growing size

x = 2
y = 2

# 0 - up, 1 - right, 2 - down, 3 - left
d = 0

dir_x = [0,1,0,-1]
dir_y = [-1,0,1,0]

a_loaded = True
b_loaded = True

last_tick = input.running_time()

def draw():
    for i in range(5):
        for j in range(5):
            if i == x and j == y:
                led.plot(i,j)
            else:
                led.unplot(i, j)

def move():
    global x,y
    x = (x + dir_x[d] + 5) % 5
    y = (y + dir_y[d] + 5) % 5

def turn(value):
    global d
    d = (d + value + 4) % 4

def check_presses():
    global a_loaded, b_loaded

    if input.button_is_pressed(Button.A):
        if a_loaded:
            a_loaded = False
            turn(-1)
    else:
        a_loaded = True

    if input.button_is_pressed(Button.B):
        if b_loaded:
            b_loaded = False
            turn(1)
    else:
        b_loaded = True

def tick(ms):
    global last_tick

    if input.running_time() - last_tick > ms:
        move()
        last_tick = input.running_time()


while True:
    draw()
    tick(300)
    check_presses()