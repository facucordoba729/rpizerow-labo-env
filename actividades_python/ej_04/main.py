import os
import time
import ADS1x15
import math
from gpiozero import PWMLED

ADS = ADS1x15.ADS1115(1, 0x48)

print(os.path.basename(__file__))
print("ADS1X15_LIB_VERSION: {}".format(ADS1x15.__version__))

ADS.setGain(ADS.PGA_4_096V)
f = ADS.toVoltage()

k = 0.2

blue = PWMLED(26)
red = PWMLED(19)

while True :
    valor_termistor = ADS.readADC(1)
    valor_potenciometro = ADS.readADC(3)
    voltaje_termistor = valor_termistor * f

    temperatura_potenciometro = 30 * valor_potenciometro / 32767.5
    resistencia_termistor = (voltaje_termistor * 10000) / (3.3 - voltaje_termistor)
    temperatura_termistor = (298 * 3900) / (298 * math.log(resistencia_termistor / 10000) + 3900) - 273.15

    print(temperatura_termistor)
    print(temperatura_potenciometro)

    diferencia = temperatura_termistor - temperatura_potenciometro

    if diferencia > 0:
        if diferencia >= 5:
            diferencia = 5
        blue.value = diferencia * k
        red.off()
    elif diferencia < 0:
        if diferencia <= -5:
            diferencia = -5
        red.value = diferencia * k * -1
        blue.off()


    time.sleep(1)
