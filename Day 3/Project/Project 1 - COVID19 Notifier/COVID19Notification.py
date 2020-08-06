import requests
from win10toast import ToastNotifier
import json
import time

def Notification():
    req = requests.get('https://coronavirus-19-api.herokuapp.com/countries/india')
    data = req.json()
    text = f'Confirmed Cases: {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("COVID-19 Notification", text, duration=10)
        time.sleep(2)
    
Notification()