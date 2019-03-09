import RPi.GPIO as GPIO
import random
import time
import asyncio

""" A lil program that converts a string to an LED blinking Morse Code"""

# a dictionary of morse characters I'll reference later
MorseDict = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ',':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', ' ': ' '} 

def set_up_gpio():
    try:
        GPIO.cleanup()
        
        # Setting up GPIO Pins
        GPIO.setmode(GPIO.BOARD)

        # I'm setting up all three so I can use an rgb led
        GPIO.setup(11,GPIO.OUT)
        GPIO.output(11,1)
        GPIO.setup(13,GPIO.OUT)
        GPIO.output(13,1)
        GPIO.setup(15,GPIO.OUT)
        GPIO.output(15,1)
    except:
        GPIO.cleanup()
        set_up_gpio()

# converts text to dots and dashes
def convert_to_morse(text):
    morse = []
    upper_text = text.upper()
    for char in upper_text:
        morse.append(MorseDict[char])
    return morse

# parses dots, dashes, and spaces, and appropriately blinks an LED
def blink_morse_character(char):
    if (char == '.'):
        print('dot')
        # light on
        # comment one or a couple out to choose color
        # GPIO.output(11, 0) # Red
        GPIO.output(13, 0) # Green
        # GPIO.output(15, 0) # Blue
        time.sleep(.2)
        # light off
        GPIO.output(11, 1)
        GPIO.output(13, 1)
        GPIO.output(15, 1)
        time.sleep(.1)            
    elif (char == '-'):
        print('dash')
        # light on
        # comment one or a couple out to choose color
        GPIO.output(11, 0) # Red
        GPIO.output(13, 0) # Green
        GPIO.output(15, 0) # Blue
        time.sleep(.5)
        # light off
        GPIO.output(11, 1)
        GPIO.output(13, 1)
        GPIO.output(15, 1)
        time.sleep(.1)
    elif(char == ' '):
        print('space')
        time.sleep(.5)

async def blink_morse_message(text):
    morse = convert_to_morse(text)
    for letter in morse:
                for char in letter:
                    blink_morse_character(char)
                time.sleep(.5)

# starts a loop that waits for input and converts it to morse in LED blinks
def convert_input_to_morse():
    keep_going = True
    try:
        while keep_going:
            text = input("Enter some text: ")
            morse = convert_to_morse(text)
            print(morse)
            blink_morse_message(morse)
                
    except KeyboardInterrupt:
        GPIO.cleanup()
        keep_going = False
