import ufirebase as fb
from machine import Pin, PWM, ADC
import time, network

def map(valCon, valMax, valMin):
    valObt = (valCon * valMax)/valMin
    return round(valObt)

wifi = network.WLAN(network.STA_IF)
if not wifi.isconnected():
    wifi.active(True)
    wifi.connect('Los Fuquene', '#*Chunt4m3*#')
    print("Contectado a la red")
else:
    print("Ya se encontraba conectado")

fHz = 10000
ledR = PWM(Pin(23), fHz)
ledG = PWM(Pin(22), fHz)
ledB = PWM(Pin(21), fHz)
pinPote = Pin(32, Pin.IN)
pote = ADC(pinPote)
pote.atten(ADC.ATTN_11DB)

fb.setURL("https://labfirebase-b3f75-default-rtdb.firebaseio.com/")

def RGB(rojo, verde, azul):
    ledR.duty(map(rojo, 1023, 255))
    ledG.duty(map(verde, 1023, 255))
    ledB.duty(map(azul, 1023, 255))
    
while True:
  fb.get("labFirebase/RGB/Blue", "var3", bg = 0)
  fb.get("labFirebase/RGB/Green", "var2", bg = 0)
  fb.get("labFirebase/RGB/Red", "var1", bg = 0)
  cantRojo = int(fb.var1)
  cantVerde = int(fb.var2)
  cantAzul = int(fb.var3)
  RGB(cantRojo, cantVerde, cantAzul)
  vlrPote = pote.read()
  fb.put("labFirebase/Poten", vlrPote, bg=0)