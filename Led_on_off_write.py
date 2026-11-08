from machine import Pin
import time

# Opsæt LED på pin 0
led = Pin(0, Pin.OUT)

print("Skriv 'on' for at tænde LED'en og 'off' for at slukke den.")

while True:
    command = input("Kommando: ").strip().lower()  # Læs brugerinput fra terminalen

    if command == "on":
        led.value(1)
        print("LED tændt 💡")
    elif command == "off":
        led.value(0)
        print("LED slukket 💤")
    else:
        print("Ugyldig kommando. Skriv 'on' eller 'off'.")
