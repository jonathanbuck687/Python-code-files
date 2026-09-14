from gpiozero import LED
from time import sleep
green = LED(17)
import random

from gpiozero import Button
button = Button(5)
button2 = Button(18)
import tm1637
import time
import numpy as np
tm = tm1637.TM1637(clk=24, dio=25)
clear = [0,0,0,0]
tm.write(clear)
while True:
    if button.is_pressed:
        rand = [random.randint(0, 9),random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
        tm.numbers(rand[0] * 10 + rand[1], rand[2] * 10 + rand[3],  colon=False)
        if (rand[0] == rand[1] and rand[0] == rand[2] and rand[0] == rand[3]):
            i = 0  
            while (i < 5):
                green.on()
                sleep(0.25)
                green.off()
                sleep(0.25)
                i = i + 1
        sleep(0.5)
    if button2.is_pressed:
        rand = [random.randint(0, 3),random.randint(0, 3), random.randint(0, 3), random.randint(0, 3)]
        tm.numbers(rand[0] * 10 + rand[1], rand[2] * 10 + rand[3],  colon=False)
        if (rand[0] == rand[1] and rand[0] == rand[2] and rand[0] == rand[3]):
            i = 0  
            while (i < 5):
                green.on()
                sleep(0.25)
                green.off()
                sleep(0.25)
                i = i + 1
        sleep(0.5)
