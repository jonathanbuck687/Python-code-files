# Dim the LED lab
from gpiozero import PWMLED
from time import sleep
from gpiozero import RotaryEncoder

led = PWMLED(18)

rotor = RotaryEncoder(16, 20, wrap=True, max_steps=180)

while True:
	led.value = (rotor.steps/180)**2
	sleep(1)
