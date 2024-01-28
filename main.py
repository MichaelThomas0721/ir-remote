import RPi.GPIO as GPIO
from time import time
import time as t

def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def binary_aquire(pin, duration):
    # aquires data as quickly as possible
    t0 = time()
    results = []
    while (time() - t0) < duration:
        results.append(GPIO.input(pin))
    return results

def send_ir_signal(bin_signal, pin):
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 38000)  # 38kHz frequency
    pwm.start(0)  # start PWM with 0% duty cycle

    for bit in bin_signal:
        if bit == '1':
            pwm.ChangeDutyCycle(50)  # send "mark"
        else:
            pwm.ChangeDutyCycle(0)  # send "space"
        time.sleep(0.0005)  # wait for a standard duration

    pwm.stop()  # stop the PWM signal


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
        bin_signal = bin(int(outbin, 2))[2:]  # convert to binary string
        send_ir_signal(bin_signal, 3)  # send the IR signal using the transmitter on pin 3
        return int(outbin, 2)
    except ValueError:
        # probably an empty code
        return None

    send_ir_signal(bin_signal, 3)


def destroy():
    GPIO.cleanup()

def on_edge_detected(channel):
    code = on_ir_receive(channel)
    if code:
        with open('decoded_ir_signal.txt', 'w') as file:
            # Write the decoded IR signal to the file
            file.write(str(code))
        print(str((code)))
    else:
        print("Invalid code")


if __name__ == "__main__":
    setup()
    try:
        print("Starting IR Listener")
        GPIO.add_event_detect(8, GPIO.FALLING, callback=on_edge_detected)
        while True:
            t.sleep(0.1)  # wait here so that the program doesn't end immediately
    except KeyboardInterrupt:
        pass
    print("Quitting")
    destroy()