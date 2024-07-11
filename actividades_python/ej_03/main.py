from gpiozero import LED, Buzzer
from time import sleep

led1= LED(13) #rojo
led2= LED(19) #verde #creo
led3= LED(26) #azul  #creo
buzz= Buzzer(22)

while True:
    comando = input("ingrese su COMANDO: ")
    opcion=input("ingrese la OPCION ")
    if comando ==  'buzz':
        if opcion== 'on':
            buzz.on()
        elif opcion=='off':
            buzz.off()

    if comando=='rgb':
        if opcion=='red':
            led1.on()
        if opcion=='blue':
            led2.on()
        if opcion=='green':
            led3.on()
