from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def fifth():
    W = white
    O = nothing
    B = blue
    logo = [
    B, B, B, B, O, O, O, O,
    B, B, B, B, O, O, O, O,
    O, B, B, O, O, O, O, O,
    O, O, O, O, O, O, O, B,
    O, O, O, O, O, O, B, B,
    O, O, O, O, O, B, B, B,
    O, O, O, O, O, B, B, B,
    O, O, O, O, O, O, B, B,
    
    ]
    return logo

def fourth():
    W = white
    O = nothing
    B = blue
    logo = [
    O, B, B, O, O, O, O, O,
    O, O, O, O, O, O, O, B,
    O, O, O, O, O, O, B, B,
    O, O, O, O, O, B, B, B,
    O, O, O, O, O, B, B, B,
    O, O, O, O, O, O, B, B,
    O, O, B, O, O, O, O, O,
    O, B, B, O, O, O, O, O,
    ]
    return logo

def third():
    W = white
    O = nothing
    B = blue
    logo = [
    O, O, O, O, O, O, B, B,
    O, O, O, O, O, B, B, B,
    O, O, O, O, O, B, B, B,
    O, O, O, O, O, O, B, B,
    O, O, B, O, O, O, O, O,
    O, B, B, O, O, O, O, O,
    B, B, B, B, O, O, O, O,
    B, B, B, B, O, O, O, O,
    ]
    return logo

def second():
    W = white
    O = nothing
    B = blue
    logo = [
    O, O, O, O, O, B, B, B,
    O, O, O, O, O, O, B, B,
    O, O, B, O, O, O, O, O,
    O, B, B, O, O, O, O, O,
    B, B, B, B, O, O, O, O,
    B, B, B, B, O, O, O, O,
    O, B, B, O, O, O, O, O,
    O, O, O, O, O, O, O, B,
    ]
    return logo

def first():
    P = pink
    O = nothing
    B = blue
    logo = [
    O, O, B, O, O, O, O, O,
    O, B, B, O, O, O, O, O,
    B, B, B, B, O, O, O, O,
    B, B, B, B, O, O, O, O,
    O, B, B, O, O, O, O, O,
    O, O, O, O, O, O, O, B,
    O, O, O, O, O, O, B, B,
    O, O, O, O, O, B, B, B,
    ]
    return logo

images = [first, second, third, fourth, fifth]
count = 0
loop = True
def raining():
    global count
    global loop
    while loop == True: 
        s.set_pixels(images[count % len(images)]())
        time.sleep(.75)
        count += 1
        if count == 20:
            count = 0
            loop = False

def pushed_up(event):
    global loop
    loop = True
    if event.action != ACTION_RELEASED:
        raining()

def pushed_down(event):
    global loop
    if event.action != ACTION_RELEASED:
        s.clear()
        loop = False


s.stick.direction_up = pushed_up
s.stick.direction_down = pushed_down
pause()