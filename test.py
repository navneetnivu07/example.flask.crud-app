import requests

r = "400,25,15.00,30.90,0"

values = r.split(',')

r = requests.post('https://a6c5cbdab06c.ngrok.io/sensor', data = {'co': values[0], 'tvoc': values[1], 'hum': values[2], 'temp': values[3], 'vib': values[4]})

print(r)

def add_two_numbers(a, b):
    return a + b

@app.route("/sensor", methods=["GET", "POST"])
def sensor():
    if request.method == "GET":
        return "Hello, World!"
    elif request.method == "POST":
        return "Hello, World!"

def diff_between_two_dates(date1, date2):
    date1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    return abs(date1 - date2).total_seconds()


