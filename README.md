# Micropython---1EMA

link do Wokwi:
https://wokwi.com/projects/474598560131544065

link wokwi modificado:
https://wokwi.com/projects/474599876659987457

código: 

'''
#Exemplo MQTT

import network
import time
import json
import random

from umqtt.simple import MQTTClient

SSID = "Wokwi-GUEST"
PASSWORD = ""

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_CLIENT_ID = "esp32_fiap_01"
MQTT_TOPIC = "fiap/iot/grupo01/temperatura"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

print("Conectando ao Wi-Fi...")

while not wifi.isconnected():
    time.sleep(0.5)

print("Wi-Fi conectado!")

client = MQTTClient(
    MQTT_CLIENT_ID,
    MQTT_BROKER,
    port=MQTT_PORT
)

print("Conectando ao broker MQTT...")

client.connect()

print("MQTT conectado!")
print("Topico:", MQTT_TOPIC)

while True:
    temperatura = round(random.uniform(20, 30), 1)

    dados = {
        "temperatura": temperatura
    }

    mensagem = json.dumps(dados)

    client.publish(MQTT_TOPIC, mensagem)

    print("Publicado:", mensagem)

    time.sleep(5)
'''


'''

#Exemplo para requisição do HTTP para dados do OpenWeather

import network
import urequests
import time

SSID = "Wokwi-GUEST"
PASSWORD = ""

API_KEY = "95b9032223fe7edc7bab00e20dc102a0"
CIDADE = "Sao%20Paulo"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

print("Conectando ao Wi-Fi...")

while not wifi.isconnected():
    time.sleep(0.5)

print("Wi-Fi conectado!")

url = (
    "https://api.openweathermap.org/data/2.5/weather"
    "?q=" + CIDADE +
    "&appid=" + API_KEY +
    "&units=metric"
)

print("URL:")
print(url)

response = urequests.get(url)

print("Status:", response.status_code)
print("Resposta:")
print(response.text)

if response.status_code == 200:
    dados = response.json()

    print()
    print("Cidade:", dados["name"])
    print("Temperatura:", dados["main"]["temp"], "C")
    print("Umidade:", dados["main"]["humidity"], "%")
    print("Condicao:", dados["weather"][0]["description"])

response.close()
'''

'''

# Exemplo para o LCD

from machine import Pin, I2C
from i2c_lcd import I2cLcd
from time import sleep

i2c = I2C(
    0,
    sda=Pin(21),
    scl=Pin(22),
    freq=400000
)

lcd = I2cLcd(i2c, 0x27, 4, 20)

lcd.move_to(0, 0)
lcd.putstr("ESP32 + MicroPython")

lcd.move_to(0, 1)
lcd.putstr("LCD 20x4")

lcd.move_to(0, 2)
lcd.putstr("I2C funcionando")

lcd.move_to(0, 3)
lcd.putstr("Wokwi - 1EMA")

while True:
    sleep(1)
'''

