# P5-DistanciaUS
## Hardware problems
We had some problems with the sensor not working randomly. We didn't know the exact issue that caused that, but sometimes whe we try to used it, it did't work, but changing the sensor to the other side of the protoboard made it work, but only one time. So we have no idea what the problem is about.

## Observations
The code is more or less the code provided, but instead of using three different leds, we decided to use a rgb led instead. We chose to use the rgb because of the three leds only one would be on at a time, so for us it make more sense to use only one that changed its color.

In order to implement the led we used the ledRGB class created in the exercise 2, so we only needed to copy the file and in the code initialize the led.
```python
ledRGB = LedRGB(rojoPin, azulPin, verdePin, inverted = True)
```
And in order to changed its color, we needed to know the distance that the sesnsor detected to change its value.
```python
duracionPulso = finPulso - inicioPulso
distancia = round(duracionPulso * 17150, 2) # In centimeters

if(distancia < 10):
    ledRGB.on(255, 0, 0) # Turn led red
elif(distancia < 20):
    ledRGB.on(255, 255, 0) # Turn led yellow
else:
    ledRGB.on(0, 255, 0) # Turn led green
```

Then the rest of the code is the same as the one given. 