import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the pin that we're going to use to read the IR sensor output
IR_SENSOR_PIN = 8

# Set the pin as an input pin
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

def binary_aquire(pin, duration):
    # aquires data as quickly as possible
    t0 = time()
    results = []
    while (time() - t0) < duration:
        results.append(GPIO.input(pin))
    return results


def on_ir_receive(pinNo, bouncetime=150):
    # when edge detect is called (which requires less CPU than constant
    # data acquisition), we acquire data as quickly as possible
    data = binary_aquire(pinNo, bouncetime/1000.0)
    if len(data) < bouncetime:
        return
    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    # detect run lengths using the acquisition rate to turn the times in to microseconds
    for i in range(1, len(data)):
        if (data[i] != data[i-1]) or (i == len(data)-1):
            pulses.append((data[i-1], int((i-i_break)/rate*1e6)))
            i_break = i
    # decode ( < 1 ms "1" pulse is a 1, > 1 ms "1" pulse is a 1, longer than 2 ms pulse is something else)
    # does not decode channel, which may be a piece of the information after the long 1 pulse in the middle
    outbin = ""
    for val, us in pulses:
        if val != 1:
            continue
        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 < us < 2000:
            outbin += "1"
    try:
        return int(outbin, 2)
    except ValueError:
        # probably an empty code
        return None


def ir_callback(channel):
    code = on_ir_receive(channel)
    with open('signal_data.txt', 'a') as f:
        f.write("IR signal received at " + time.ctime() + "\n")
        f.write(str(code))
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