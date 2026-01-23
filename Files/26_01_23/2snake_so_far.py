apple_x = 0
apple_y = 0

def spawn_apple():
    global apple_x,apple_y
    # zobrazeni jablicka
    led.unplot(apple_x,apple_y)
    apple_x = randint(0,4)
    apple_y = randint(0,4)
    led.plot(apple_x,apple_y)

player_x = 4
player_y = 3

def clear_screen():
    for x in range(5):
        for y in range(5):
            led.unplot(x, y)
 
def move():
    global player_x
    player_x = player_x - 1

input.on_button_pressed(Button.A, move)
input.on_button_pressed(Button.B, clear_screen)

while True:
    # print(player_x)
    led.plot(player_x,player_y)
    pause(100)
    # led.unplot(player_x, player_y)
    # player_x -= 1


    # pause(100)
    