from neopixel import Neopixel
from machine import Pin
import time
import random

# Knapper
button1 = Pin(26, Pin.IN, Pin.PULL_UP)
button2 = Pin(3, Pin.IN, Pin.PULL_UP)

# Vibrationsmoduler
motor1 = Pin(15, Pin.OUT)
motor2 = Pin(14, Pin.OUT)

# NeoPixel
pixels = Neopixel(5, 0, 16, "RGB")


def set_color(color):
    for i in range(5):
        pixels.set_pixel(i, color)
    pixels.show()


def stop_motors():
    motor1.off()
    motor2.off()


while True:

    print("\nNy runde")

    stop_motors()

    # Rød = vent
    set_color((255, 0, 0))

    time.sleep(random.uniform(2, 5))

    # Blå = klar
    set_color((0, 0, 255))

    time.sleep(random.uniform(1, 5))

    # Begge får vibration samtidigt
    motor1.on()
    motor2.on()

    start = time.ticks_ms()

    winner = None

    while winner is None:

        if not button1.value():

            reaction_time = time.ticks_diff(
                time.ticks_ms(),
                start
            )

            winner = "Spiller 1"

        elif not button2.value():

            reaction_time = time.ticks_diff(
                time.ticks_ms(),
                start
            )

            winner = "Spiller 2"

    stop_motors()

    print(
        f"{winner} reagerede på {reaction_time} ms"
    )

    # Vis vinder
    if winner == "Spiller 2":

        # gul 
        set_color((255, 255, 0))

    else:

        # grøn
        set_color((0, 255, 0))

    time.sleep(3)
