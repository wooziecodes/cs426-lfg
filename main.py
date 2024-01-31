
from microbit import *

while True:
    light_level = display.read_light_level()  # Read the ambient light level
    brightness = 255 - light_level  # Adjust brightness inversely to light level
    display.set_brightness(brightness)  # Set the brightness of the display
    display.show(Image.HAPPY)  # Replace with any icon you like
    sleep(100)
