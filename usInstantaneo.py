#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from ledRGB import LedRGB

rojoPin = 36
azulPin = 40
verdePin = 38

def main():
    try:
        GPIO.setmode(GPIO.BOARD)

        PIN_TRIGGER = 7
        PIN_ECHO = 11

        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)
        ledRGB = LedRGB(rojoPin, azulPin, verdePin, inverted = True)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        print( "Esperando a que se estabilice el US")
        time.sleep(2)
        while True:
            GPIO.output(PIN_TRIGGER, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(PIN_TRIGGER, GPIO.LOW)
        
        
            while GPIO.input(PIN_ECHO)==0:
                inicioPulso = time.time()
            while GPIO.input(PIN_ECHO)==1:
                finPulso = time.time()

            duracionPulso = finPulso - inicioPulso
            distancia = round(duracionPulso * 17150, 2) # In centimeters
            
            if(distancia < 10):
                ledRGB.on(255, 0, 0) # Turn led red
            elif(distancia < 20):
                ledRGB.on(255, 255, 0) # Turn led yellow
            else:
                ledRGB.on(0, 255, 0) # Turn led green
            time.sleep(0.1)
                  
    finally:
        GPIO.cleanup()


main()
