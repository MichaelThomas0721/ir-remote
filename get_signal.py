import RPi.GPIO as GPIO
from datetime import datetime
import time

# Static program vars
pin = 8  # Input pin of sensor (GPIO.BOARD)
# Sets up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)


def getSequence():
    # Internal vars
    num1s = 0  # Number of consecutive 1s read
    sequence = []  # The list to store pulse times in
    previousValue = 0  # The last value
    value = GPIO.input(pin)  # The current value

    # Waits for the sensor to pull pin low
    while value:
        time.sleep(0.0001)  # This sleep decreases CPU utilization immensely
        value = GPIO.input(pin)

    # Records start time
    startTime = datetime.now()

    while True:
        # If change detected in value
        if previousValue != value:
            now = datetime.now()
            pulseTime = now - startTime  # Calculate the time of pulse
            startTime = now  # Reset start time
            sequence.append(
                (previousValue, pulseTime.microseconds)
            )  # Store recorded data

        # Updates consecutive 1s variable
        if value:
            num1s += 1
        else:
            num1s = 0

        # Breaks program when the amount of 1s surpasses 10000
        if num1s > 10000:
            break

        # Re-reads pin
        previousValue = value
        value = GPIO.input(pin)
    return sequence




while True:
    print(getSequence())