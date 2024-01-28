import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the pin that we're going to use to read the IR sensor output
IR_SENSOR_PIN = 8

# Set the pin as an input pin
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

def ir_callback(channel):
    with open('signal_data.txt', 'a') as f:
        f.write("IR signal received at " + time.ctime() + "\n")
    print("IR signal received")

# When a change is detected on the IR_SENSOR_PIN, the ir_callback function will be run
GPIO.add_event_detect(IR_SENSOR_PIN, GPIO.BOTH, callback=ir_callback)

try:
    # Use a loop to keep the script running
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # When Ctrl+C is pressed, the script will quit
    GPIO.cleanup()