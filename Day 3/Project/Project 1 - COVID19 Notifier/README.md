# COVID 19 Notification
This is a very simple program which gives COVID19 Update to the user via desktop notification.

- In this project, the program gets the url using `request` module.
        req = requests.get('https://coronavirus-19-api.herokuapp.com/countries/india')

- Also it fetches data from `json` file using `json` module.
        data = req.json()
    text = f'Confirmed Cases: {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

- It uses `win10toast` module to give notification in Windows 10. You can install this module by `pip install win10toast`.

- I have used the APIs provided by **Javier Aviles**. You can check his repository [here](https://github.com/javieraviles/covidAPI)

#### Image of the Notification

![Image](https://github.com/saswatsamal/100DaysofPython/blob/master/Day%203/Project/Project%201%20-%20COVID19%20Notifier/COVId19Notification.png)


