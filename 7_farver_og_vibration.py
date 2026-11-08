from machine import Pin
from neopixel import Neopixel
import time

# Hardware
pixels = Neopixel(5, 0, 16, "RGB")   # 5 pixels på GP16
motor = Pin(15, Pin.OUT)             # vibrationsmotor på GP15


def clear():
    pixels.fill((0, 0, 0))
    pixels.show()


def friendly():
    pixels.fill((0, 255, 0))   # Grøn

    pixels.show()

    time.sleep(1)

    clear()


def important():
    for _ in range(3):

        pixels.fill((255, 180, 0))   # Orange

        pixels.show()

        motor.on()
        time.sleep(0.2)

        motor.off()
        clear()

        time.sleep(0.2)


def urgent():
    for _ in range(10):

        pixels.fill((255, 0, 0))     # Rød

        pixels.show()

        motor.on()

        time.sleep(0.1)

        motor.off()
        clear()

        time.sleep(0.1)


while True:

    friendly()

    time.sleep(2)

    important()

    time.sleep(2)

    urgent()

    time.sleep(2)
