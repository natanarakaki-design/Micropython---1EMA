# Micropython---1EMA

link do Wokwi:
https://wokwi.com/projects/474598560131544065

link wokwi modificado:
https://wokwi.com/projects/474599876659987457



# código: 

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

#Exemplo para o LCD

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

# Código node-red:

[
    {
        "id": "b8dd49cf8aec93e8",
        "type": "tab",
        "label": "Fluxo 1",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "0786545694bc480b",
        "type": "mqtt in",
        "z": "b8dd49cf8aec93e8",
        "name": "",
        "topic": "fiap/iot/grupo01/clima",
        "qos": "2",
        "datatype": "auto-detect",
        "broker": "d52e711810353783",
        "nl": false,
        "rap": true,
        "rh": 0,
        "inputs": 0,
        "x": 220,
        "y": 300,
        "wires": [
            [
                "e720a804e2200145"
            ]
        ]
    },
    {
        "id": "e720a804e2200145",
        "type": "json",
        "z": "b8dd49cf8aec93e8",
        "name": "",
        "property": "payload",
        "action": "obj",
        "pretty": false,
        "x": 430,
        "y": 300,
        "wires": [
            [
                "58e504a9730f49d6"
            ]
        ]
    },
    {
        "id": "58e504a9730f49d6",
        "type": "function",
        "z": "b8dd49cf8aec93e8",
        "name": "function 1",
        "func": "var dados = msg.payload;\n\n// Formata uma string organizada para exibição\nvar textoFormatado = `=== DADOS METEOROLÓGICOS ===\\n` +\n                     `Cidade: ${dados.cidade}\\n` +\n                     `Temperatura: ${dados.temperatura} °C\\n` +\n                     `Umidade: ${dados.umidade}%\\n` +\n                     `Condição: ${dados.condicao}`;\n\nmsg.payload = textoFormatado;\nreturn msg;",
        "outputs": 1,
        "timeout": 0,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 580,
        "y": 300,
        "wires": [
            [
                "a154db223d90090b"
            ]
        ]
    },
    {
        "id": "a154db223d90090b",
        "type": "debug",
        "z": "b8dd49cf8aec93e8",
        "name": "debug 1",
        "active": true,
        "tosidebar": true,
        "console": true,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "statusVal": "",
        "statusType": "auto",
        "x": 750,
        "y": 300,
        "wires": []
    },
    {
        "id": "d52e711810353783",
        "type": "mqtt-broker",
        "name": "HiveMQ",
        "broker": "broker.hivemq.com:1883",
        "port": 1883,
        "clientid": "esp32_fiap_01",
        "autoConnect": true,
        "usetls": false,
        "protocolVersion": 4,
        "keepalive": 60,
        "cleansession": true,
        "autoUnsubscribe": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthRetain": "false",
        "birthPayload": "",
        "birthMsg": {},
        "closeTopic": "",
        "closeQos": "0",
        "closeRetain": "false",
        "closePayload": "",
        "closeMsg": {},
        "willTopic": "",
        "willQos": "0",
        "willRetain": "false",
        "willPayload": "",
        "willMsg": {},
        "userProps": "",
        "sessionExpiry": ""
    }
]

# Código modificado:

import network
import urequests
import time
import json
from machine import Pin, I2C
from i2c_lcd import I2cLcd
from umqtt.simple import MQTTClient

#--- Configurações do Wi-Fi ---
SSID = "Wokwi-GUEST"
PASSWORD = ""

#--- Configurações da OpenWeather ---
API_KEY = "95b9032223fe7edc7bab00e20dc102a0"
CIDADE = "Sao%20Paulo"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

#--- Configurações MQTT ---
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_CLIENT_ID = "esp32_fiap_01"
MQTT_TOPIC = "fiap/iot/grupo01/clima"

#--- Inicialização do I2C e LCD ---
i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
lcd = I2cLcd(i2c, 0x27, 4, 20)

#--- Conexão Wi-Fi ---
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

lcd.clear()
lcd.putstr("Conectando Wi-Fi...")

while not wifi.isconnected():
    time.sleep(0.5)

lcd.clear()
lcd.putstr("Wi-Fi Conectado!")
time.sleep(1)

#--- Conexão MQTT ---
lcd.clear()
lcd.putstr("Conectando MQTT...")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
client.connect()

lcd.clear()
lcd.putstr("MQTT Conectado!")
time.sleep(1)

#--- Loop Principal ---
while True:
    try:
        #1. Requisição HTTP para OpenWeather
        response = urequests.get(URL)
        
        if response.status_code == 200:
            dados = response.json()
            
            cidade = dados["name"]
            temp = dados["main"]["temp"]
            umidade = dados["main"]["humidity"]
            descricao = dados["weather"][0]["description"]
            
            response.close()

            # 2. Atualização do LCD 20x4
            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr(f"Cidade: {cidade[:12]}")
            
            lcd.move_to(0, 1)
            lcd.putstr(f"Temp: {temp:.1f} C")
            
            lcd.move_to(0, 2)
            lcd.putstr(f"Umidade: {umidade}%")
            
            lcd.move_to(0, 3)
            lcd.putstr(f"Tempo: {descricao[:13]}")

            # 3. Preparação do JSON e Envio via MQTT
            payload = {
                "cidade": cidade,
                "temperatura": temp,
                "umidade": umidade,
                "condicao": descricao
            }
            
            client.publish(MQTT_TOPIC, json.dumps(payload))
            print("Publicado:", json.dumps(payload))
            
        else:
            print("Erro HTTP:", response.status_code)
            response.close()

    except Exception as e:
        print("Erro na execução:", e)

    #Atualiza a cada 10 segundos (limite de requisições da API)
    time.sleep(10)

    
