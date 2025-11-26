import time
import board
import neopixel
from flask import Flask
import random


pixel_pin = board.D18
num_pixels = 45
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

app = Flask(__name__)

@app.route('/')
def display_start():
    return "Roulette!"

@app.route('/lucky')
def led_bounce():
    rounds_random = random.randint(4,8)
    #print(rounds_random)
    number_random = random.randint(0,44)
    #print(number_random)
    wait = 0.002


    for r in range(rounds_random):
        if r%2 == 0:
            wait += 0.0002
            print (wait)
        for b in range(num_pixels):
            pixels[b] = (255, 255, 255)
            pixels.write()
            time.sleep(wait)
            pixels[b] = (0, 0, 0)
            time.sleep(wait)
            wait += 0.0001
            #print(r)

    for n in range(number_random):
        print(n)
        print(wait)
        pixels[n] = (255, 255, 255)
        pixels.write()
        time.sleep(wait)
        pixels[n] = (0, 0, 0)
        time.sleep(wait)
        if number_random <= 10:
            wait += (wait + 0.000001) - wait * 0.5
        elif wait <= 20:
            wait += (wait + 0.000001) - wait * 0.95
        elif wait <= 30:
            wait += (wait + 0.000001) - wait * 0.999
        else:
            wait += (wait + 0.000001) - wait * 0.9999

    return f"The winning number is: {number_random} "

if __name__ == '__main__':
    app.run(host='192.168.68.96')
