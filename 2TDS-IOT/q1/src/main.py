import network
import urequests
import time
import json
from machine import Pin, I2C
from i2c_lcd import I2cLcd
from umqtt.simple import MQTTClient


SSID = "Wokwi-GUEST"
PASSWORD = ""


API_KEY = "95b9032223fe7edc7bab00e20dc102a0"
CIDADE = "Sao%20Paulo"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"


MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_CLIENT_ID = "esp32_fiap_01"
MQTT_TOPIC = "fiap/iot/grupo01/clima"


i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
lcd = I2cLcd(i2c, 0x27, 4, 20)


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


lcd.clear()
lcd.putstr("Conectando MQTT...")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
client.connect()

lcd.clear()
lcd.putstr("MQTT Conectado!")
time.sleep(1)


while True:
    try:
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

    time.sleep(10)