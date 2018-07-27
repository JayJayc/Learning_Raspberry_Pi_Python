from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

blue = (0, 0, 255)
red = (255, 0, 0)

temp = sense.get_temperature()
print(int(temp))

printOut = "Temperature is "+str(int(temp))

while True:
  sense.show_message(printOut, text_colour=red, back_colour=blue, scroll_speed=0.2)

