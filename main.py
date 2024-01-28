import RPi.GPIO as GPIO
from time import time

# Numbers GPIOs by physical location
GPIO.setmode(GPIO.BOARD)
# set pin 8 as an input pin with default as LOW v
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# define a function to acquire data
def binary_acquire(pin):
    # acquires data as quickly as possible
    while True:
        result = GPIO.input(pin)
        if result:
            return result

print("Waiting for input...")
# acquire data
result = binary_acquire(8) # changed pin number to 8
print("Input received!")
print(result)
GPIO.cleanup()