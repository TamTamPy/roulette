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

co_authors = ["AnomaLi", "Christian"]

number_excluded = [4,8,12,17,26,31,35,39]
numbers_included = [i for i in range(0, 45) if i not in number_excluded]
dict_numbers_valid = {

    0:0,
    1:32,
    2:15,
    3:19,
    5:4,
    6:21,
    7:2,
    9:25,
    10:17,
    11:34,
    13:6,
    14:27,
    15:13,
    16:36,
    18:11,
    19:30,
    20:8,
    21:23,
    22:10,
    23:5,
    24:24,
    25:16,
    27:33,
    28:1,
    29:20,
    30:14,
    32:31,
    33:9,
    34:22,
    36:18,
    37:29,
    38:7,
    40:28,
    41:12,
    42:35,
    43:3,
    44:26

    }

### einfache Chancen ###

rouge = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
noir = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
impair = [i for i in range(1, 37) if i % 2 == 1]
pair = [i for i in range(1, 37) if i % 2 == 0]
manque = list(range(1,19))
passe = list(range(19,37))





@app.route('/')
def display_start():

    return f"Roulette! \n I thank my Co-Authors:"



@app.route('/lucky')
def led_bounce():
    rounds_random = random.randint(4,8)
    #print(rounds_random)
    number_random = random.choice(numbers_included)
    print(number_random)
    print(numbers_included)
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


        if dict_numbers_valid.get(number_random) in rouge:
            return f"{dict_numbers_valid.get(number_random)} Rouge"
        elif dict_numbers_valid.get(number_random) in noir:
            return f"{dict_numbers_valid.get(number_random)} Noir"



if __name__ == '__main__':
    app.run(host='192.168.178.159')
