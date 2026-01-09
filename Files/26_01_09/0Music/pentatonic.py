import microbit as mb
import music

frequencies = [
    261,  # C4
    293,  # D4
    329,  # E4
    392,  # G4
    440,  # A4
]

class JustPressedWrapper:

    def __init__(self, event):
        self.loaded = True
        self.event = event
    
    def is_just_pressed(self) -> bool:
        if self.event():
            if self.loaded:
                self.loaded = False
                return True
        else:
            self.loaded = True
        return False

butt_a = JustPressedWrapper(mb.button_a.is_pressed)
butt_b = JustPressedWrapper(mb.button_b.is_pressed)
touchpad = JustPressedWrapper(mb.pin_logo.is_touched)

def render_display(x : int):
    for i in range(5):
        if i == x:
            mb.display.set_pixel(i,4,9)
        else:
            mb.display.set_pixel(i,4,0)

x = 0

while True:
    if butt_b.is_just_pressed():
        x += 1
        if x > 4:
            x = 0
    if butt_a.is_just_pressed():
        x -= 1
        if x < 0:
            x = 4

    if touchpad.is_just_pressed():
        music.pitch(frequencies[x],100,wait = False)

    render_display(x)