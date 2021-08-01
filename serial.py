import serial
import requests
CO2 = []
TVOC = []
Vib = []
Temp = []
Hum = []
date_time = []
 
ser = serial.Serial('/dev/ttyACM0',9600,timeout = 5)
while  True:
    try:
        r = ser.readline().decode("utf-8") 
        r = "400,25,55.00,30.90,0"
        print(r)
        values=r.split(",")
        r = requests.post('https://a6c5cbdab06c.ngrok.io/sensor', data = {'co': values[0], 'tvoc': values[1], 'hum': values[2], 'temp': values[3], 'vib': values[4]})

    except KeyboardInterrupt:
        break