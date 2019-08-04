#!/usr/bin/python3
"""
Name: Kapish Soma
Student Number: SMXKAP001
Prac: 1
Date: 28/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO

# Logic that you write
#def display(count):
    
    
    


def main():
    count = 0;                          #Set count to 0
    print(count)                        #Show count
    GPIO.setmode(GPIO.BOARD)            #Set numbering scheme to Board
    GPIO.setup(32, GPIO.OUT)            #Set pin 32,36 & 38 to output
    GPIO.setup(36, GPIO.OUT)
    GPIO.setup(38, GPIO.OUT)
    GPIO.output(32, 0)                  #Initially pins must be all off
    GPIO.output(36, 0)
    GPIO.output(38, 0)
    
    GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP)         #Initialise PUP resistors
    GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(35, GPIO.FALLING, bouncetime=300)   #Add interupts for both buttons 
    GPIO.add_event_detect(37, GPIO.FALLING, bouncetime=300)
    
    import itertools
    lst = list(itertools.product([0, 1], repeat=3))
    
        
    while True:
        
        if GPIO.event_detected(35)== True:          #Check for falling edge as Pull-up is  used
            count = count + 1                       #Count increases by 1
            if count > 7:                           #For the wrap around condition
                count = 0
            print(count)
            print(lst[count])
            GPIO.output(32, lst[count][0])          #Output to LED's
            GPIO.output(36, lst[count][1])    
            GPIO.output(38, lst[count][2])
               
    
        if GPIO.event_detected(37)==True:
            count = count - 1
            if count < 0:
                count = 7
            print(count)
            print(lst[count])
            GPIO.output(32, lst[count][0])          #Output to LED's
            GPIO.output(36, lst[count][1])    
            GPIO.output(38, lst[count][2])


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
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
