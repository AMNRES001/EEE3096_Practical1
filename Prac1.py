


#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Reshad Amin
Student Number: AMNRES001
Prac: 1
Date: 03/08/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

# initialize specific GPIO ports to input and output
GPIO.setup(7, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(11, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# initializing global variables in the function and setting intial values
pinNum = 0
count = 0
index = 0
x = 0

#defining the counter function to increment and decrement
def pushbuttons():
	global count
	if (GPIO.input(35) == 1 and count != 7):
                count += 1)
                time.sleep(1)
	if (GPIO.input(35) == 1 and count == 7):
                count = 0
                time.sleep(1)
	if (GPIO.input(36) == 1 and count != 0):
                count -= 1
                time.sleep(1)
	if (GPIO.input(36) == 1 and count == 0):
                count = 7
                time.sleep(1)
		#return

#turn LEDs off
def lightOff(pinNum):
        if (pinNum == 0):
                GPIO.output(7, GPIO.LOW)
        if (pinNum == 1):
                GPIO.output(11, GPIO.LOW)
        if (pinNum == 2):
                GPIO.output(13, GPIO.LOW)
        #return

#turn LEDs on
def lightON(pinNum):
        if (pinNum == 0):
                GPIO.output(7, GPIO.HIGH)
        if (pinNum == 1):
                 GPIO.output(11, GPIO.HIGH)
        if (pinNum == 2):
                GPIO.output(13, GPIO.HIGH)
        #return

def lights(x):
	binarystring = bin(x)[2:].zfill(3)
	for index, value in enumerate(binarystring):
		if (value == '1'):
			lightOn(index)
		else:
			lightOff(index)
		#return

# Logic that you write
def main():
    pushbuttons()
    lights(count)


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)

