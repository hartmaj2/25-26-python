# --- GLOBAL VARIABLES ---

ax = 0
ay = 0

pxs = [2]
pys = [2]

dirc = 1
dir_to_cord = [[0,-1],[1,0],[0,1],[-1,0]]

# --- VISUALS ---

def clear_screen():
    for i in range(5):
            for j in range(5):
                led.unplot(i,j)

def draw(x,y,b):
    led.plot_brightness(x, y, b)

def draw_snake():
    global pxs,pys
    for i in range(len(pxs)):
        draw(pxs[i],pys[i],255)

def draw_apple():
    global ax,ay
    draw(ax,ay,128)

# --- MOVEMENT ---

def wraparound_all():
    for i in range(len(pxs)):
        pxs[i] = (pxs[i] + 5) % 5
        pys[i] = (pys[i] + 5) % 5

def move():
    global pxs,pys
    for i in range(len(pxs)-1,-1,-1):
        if i == 0: # move the snake head
            pxs[i] += dir_to_cord[dirc][0]
            pys[i] += dir_to_cord[dirc][1]
        else:
            pxs[i] = pxs[i-1]
            pys[i] = pys[i-1]

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

# --- GAME LOGIC ---

def spawn_apple():
    global ax,ay
    ax = randint(0,4)
    ay = randint(0,4)

spawn_apple()

while True:

    clear_screen()
    draw_apple()
    draw_snake()
    
    pause(500)

    move()
    wraparound_all()

    if pxs[0] == ax and pys[0] == ay:
        pxs.push(pxs[0])
        pys.push(pys[0])
        spawn_apple()
