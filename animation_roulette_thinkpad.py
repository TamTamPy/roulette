import time
import board
import neopixel
from flask import Flask


pixel_pin = board.D18
num_pixels = 45
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

app = Flask(__name__)

def led_Bounce():
    for i in range(num_pixels):
        pixels[i] = (255, 255, 255)
        pixels.write()
        time.sleep(1)
        pixels[i] = (0, 0, 0)
        time.sleep(1)


if __name__ == '__main__':
    try:
        while True:
            led_Bounce()
    except KeyboardInterrupt:
        print("this is the end")