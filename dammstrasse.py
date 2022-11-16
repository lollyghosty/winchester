import requests
s_city = "Moscow,RU"
appid = "c25e8da9ebff9b8a084ab48b94b98152"
restoday = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data1 = restoday.json()

print("Прогноз погоды на день:")
print("Город:", s_city)
print("Погодные условия:", data1['weather'][0]['description'])
print("Температура:", data1['main']['temp'])
print("Минимальная температура:", data1['main']['temp_min'])
print("Максимальная температура", data1['main']['temp_max'])
print("____________________________")

resweek = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data2 = resweek.json()
print("Прогноз погоды на неделю:")
for i in data2['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
'{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
i['weather'][0]['description'], ">")
print("____________________________")

print("Прогноз ветра и видимости на сегодня:")
print('Cкорость ветра: ', data1['wind']['speed'], ' м/с')
print("Видимость: ", (data1['visibility'] / 10000)*100, '%')
print("_______________________git_____")

print("Прогноз ветра и видимости на неделю:")
for i in data2["list"]:
    print("Дата: ", i['dt_txt'],
    "\r\n Скорость ветра: ", i['wind']['speed'], ' м/с',
    "\r\n Видимость: ", round((i['visibility'] / 10000)*100), '%')
print("____________________________")

