from machine import Pin
from time import sleep

motor = Pin(15, Pin.OUT)

while True:
    motor.on()      # vibration ON
    sleep(0.5)

    motor.off()     # vibration OFF
    sleep(0.5)
