# import libraries
import RPi.GPIO as GPIO  # Rpi.gpio the package that allows us to interact with GPIO pins
import time  # control time related functions: i.e. sleep and time how long it takes to receive data
import datetime

while (1 == 1): ###ENABLES INFINITE LOOP
      try:  # try covers the majority of the code and ensure that we clear gpio pins on exit
            GPIO.setmode(GPIO.BOARD)  # using physical pins numbers and not the BCM numbers

            PIN_TRIGGER = 7  # variables to store physical pins
            PIN_ECHO = 11  # variable

            GPIO.setup(PIN_TRIGGER, GPIO.OUT)  # trigger pin is output, using to ping this pin to start the sensor
            GPIO.setup(PIN_ECHO, GPIO.IN)  # echo pin where we expect out data from

            GPIO.output(PIN_TRIGGER, GPIO.LOW)  # Set PIN_TRIGGER to low to let the sensor to settle, more consistent readings

            #print ("Waiting for sensor to settle")  # ""
            time.sleep(1)  # "" , giving the distance sensor enough time to settle
            #print ("Calculating distance")
            GPIO.output(PIN_TRIGGER, GPIO.HIGH)  # trigger the sensor by setting to high
            time.sleep(0.00001)  # need to sleep the script for 1 nanosecond, the sensor requires a pulse of 1 nanosecond to trigger
            GPIO.output(PIN_TRIGGER, GPIO.LOW)  # Once sleep has completed, set pin trigger to low
            while GPIO.input(PIN_ECHO)==0:  # run a while loop to check if Pin_Echo is low(0)
                                            # If it is, we continually set the pulse_start_time to the current time until it becomes high(1)
                  pulse_start_time = time.time()
            while GPIO.input(PIN_ECHO)==1:
                  pulse_end_time = time.time()
            # these loops allow us to calculate the time it took for the sensor pulse to be sent out and received back
            # When we have both times, we have to minus the two saved times to work out the duration
            # w/ pulse duration calculated we can work out the distance it traveled since we know ultrasonic speed is ~ 34300cm/s
            pulse_duration = pulse_end_time - pulse_start_time  # duration of the pulse is the time it took for the ultrasonic sound to hit an object and bounce back...
                                                                # we need half the speed to calculate the speed to calculate the distance it traveled
            distance = round(pulse_duration * 17150, 2) # calucating the distance with the full speed then divide by 2
                                                            # distance is equal to the duration of the pulse, * 17150cm/s
            #print("Pulse Duration:",pulse_duration, "seconds")
            #print("Pulse Start Time:", pulse_start_time, "seconds")
            print ("Distance:",distance,"cm")

            if distance < 70:
                  print("SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT")
                  print("SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT")
                  print("SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT")
                  print("SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT")
                  print("SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT")
                  print("SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT")
                  print("SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT")
                  print("SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT")
                  print("SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT")
                  print("SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT")
                  print("SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT")
                  print("SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT SOMEBODY IS HERE LOOK OUT")
                  print(datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S"))
                  time.sleep(30)

            #else:
                      #print("SOMEBODY IS HERE!!!!!!!!!!!!!!!")

      finally:
            GPIO.cleanup()  # ensures an end to the try: statement and that we run cleanup when the script is terminated in anyway
                            # failing to do this will throw warnings when retunning the script or any other script that makes useof the GPIO pins
                      #time.sleep(30)