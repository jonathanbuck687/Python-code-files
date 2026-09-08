
from gpiozero import LED
from time import sleep

red = LED(17)
blue = LED(18)


import time
import board
import adafruit_dht
from datetime import datetime

sensor = adafruit_dht.DHT11(board.D16) # Change the pin number to the data pin of your DHT11 

print("time,celsius,fahrenheit")

def to_fahrenheit(c):
    # TODO: Assign f where f represents the Farienheit equivalent to the input Celcius c
    f = c * (9/5) + 32
    return f 

while True:
    try:
        celsius = sensor.temperature # Get the temperature in Celcius from the sensor
        fahrenheit = to_fahrenheit(celsius)
        current_time = datetime.now()
        with open("temperature.csv","a") as file:
            file.write("{0},{1:0.1f},{2:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))
            file.write("\n")
                    
        if (fahrenheit < 72):
            red.off()
            blue.on()
        else:
            blue.off()
            red.on()
        # TODO: Light up the red light when the temperature is above 72, and blue when it is below 72.
        time.sleep(3.0)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except KeyboardInterrupt:
        GPIO.cleanup()
    except Exception as error:
        sensor.exit()
        raise error    
