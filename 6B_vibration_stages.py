from machine import Pin, PWM
from time import sleep

motor = PWM(Pin(15))

motor.freq(1000)

while True:

    # svag vibration
    motor.duty_u16(10000)
    sleep(2)

    # kraftig vibration
    motor.duty_u16(65535)
    sleep(2)
