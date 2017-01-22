# Kitty box control program
# John Hebert

# imports
import RPi.GPIO as GPIO
import time

# Varibles
PIR_Sensor = 11                     # Motion sensor input
LED_Lights = 3                      # PWM output for LEDs
Fan = 7                             # fan relay output
On_Time = 30                        # fan/lights delay seconds

# set up GPIO I/O pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_Sensor, GPIO.IN)
GPIO.setup(LED_Lights, GPIO.OUT)
GPIO.setup(Fan, GPIO.OUT)
PWM = GPIO.PWM(LED_Lights, 100)   # set PWM output to 0%
PWM.start(0)

# state machine
State = 0
Prev_Value = 0
Delay_Counter = 0
while True:
    Sensor = GPIO.input(PIR_Sensor) # read the PIR sensor
    
    if State == 0:              # STATE 0: evaluate sensor value
        if Sensor == 1 and Prev_Value == 0:
            State = 1           # sensor switched on. turn lights on
            Prev_Value = 1
        elif Sensor == 0 and Prev_Value == 1:
            State = 2           # sensor switched off. turn lights off
            Prev_Value = 0
            
    elif State == 1:            # STATE 1: ramp lights up and turn fan on
        print ("on")
        GPIO.output(Fan, 1)     # fan on
        for j in range(50):     # ramp the PWM output
            k = j * 2
            PWM.ChangeDutyCycle(k)
            time.sleep(0.06)
        State = 3
        
    elif State == 2:            # STATE 2: turn lights and fan off
        GPIO.output(Fan, 0)     # fan off
        PWM.ChangeDutyCycle(0)  # lights off
        State = 0
        print ("off")
        
    elif State == 3:            # STATE 3: time on delay
        time.sleep(1)           # one second
        Delay_Counter = Delay_Counter + 1
        if Sensor == 1:         # reset on time counter if sensor is triggered again
            Delay_Counter = 0
            print ("retrigger")
        if Delay_Counter >= On_Time:
            State = 0
            Delay_Counter = 0
            
    time.sleep(0.025)

GPIO.cleanup()

