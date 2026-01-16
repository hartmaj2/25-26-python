# This counter lights up a new lead per each press of the button
# Moreover another light switches on every second

x = 0
y = 0
brightness = 1

a_loaded = True

last_tick = input.running_time()

def increase():
    global x, y, brightness
    x += 1
    if x > 4:
        x = 0
        y += 1
    if y > 4:
        y = 0
        brightness += 3

def draw():
    global x,y
    # led.plot(x, y)
    # led.toggle(x, y)
    led.plot_brightness(x, y, 255*(brightness/9))

while True:
    if input.running_time() - last_tick > 1000:
        draw()
        increase()
        last_tick = input.running_time()
    if input.button_is_pressed(Button.A):
        if a_loaded:
            draw()
            a_loaded = False
            increase()
    else:
        print(a_loaded)
        a_loaded = True
