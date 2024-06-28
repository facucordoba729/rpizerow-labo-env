from gpiozero import LED
from time import sleep

led1= LED(13)
led2= LED(19)
led3= LED(26)
while True:
    led1.off()
    led2.off()
    led3.off()
    sleep(0.25)
    #0.25s
    led3.on()
    sleep(0.25)
    #0.5s
    led3.off()
    led2.on()
    sleep(0.25)
    led3.on()
    sleep(0.25)
    #0.75s
    led3.off()
    led2.off()
    led1.on()
    sleep(0.25)
    #1s
    led3.on()
    sleep(0.25)
    led3.off()
    led2.on()
    sleep(0.25)
    led3.on()
    sleep(0.25)

