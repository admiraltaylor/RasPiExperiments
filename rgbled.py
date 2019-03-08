import RPi.GPIO as GPIO
import random
import time

"""A little program that makes an rgb led put on a little rave."""


GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.output(11,1)
GPIO.setup(13,GPIO.OUT)
GPIO.output(13,1)
GPIO.setup(15,GPIO.OUT)
GPIO.output(15,1)

init_string = "000"


def set_random_color():
    GPIO.output(11, bool(random.getrandbits(1)))
    GPIO.output(13, bool(random.getrandbits(1)))
    GPIO.output(15, bool(random.getrandbits(1)))

# generate a random rgb color string for the led
def set_random_color_string(prev_rgb):
    r = int(random.getrandbits(1))
    g = int(random.getrandbits(1))
    b = int(random.getrandbits(1))

    rgb = "{}{}{}".format(r,g,b)   
    
    # if it's not "off" nor the previous color, returns it
    if rgb != prev_rgb and rgb != "111":
        print("rgb: {}".format(rgb))
        return rgb
    else: # recursion!
        return set_random_color_string(prev_rgb)  

try:

    while(True):
        init_string = set_random_color_string(init_string)
        GPIO.output(11, int(init_string[0]))
        GPIO.output(13, int(init_string[1]))
        GPIO.output(15, int(init_string[2]))
        time.sleep(.1)
        
except KeyboardInterrupt:
    GPIO.cleanup()

    
