import requests

r = "400,25,15.00,30.90,0"

values = r.split(',')

r = requests.post('https://a6c5cbdab06c.ngrok.io/sensor', data = {'co': values[0], 'tvoc': values[1], 'hum': values[2], 'temp': values[3], 'vib': values[4]})

print(r)