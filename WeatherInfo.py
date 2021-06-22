import requests

city=input("Enter Your City = ")
Api_Key = "eeeed4e6927bc2d22e1cc8a319b4f6ab" 

final_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,Api_Key)

result = requests.get(final_URL)
data = result.json()

temprature = ((data['main']['temp']) - 273.15)
hmdt = data['main']['humidity']
weather_desc = data['weather'][0]['description']
wind_spd = data['wind']['speed']
cordinatelon = data['coord']['lon']
cordinatelat = data['coord']['lat']

print("temprature:",temprature,)
print("hmdt:",hmdt,)
print("weather_desc:",weather_desc,)
print("wind_spd:",wind_spd,)
print("cordinatelon:",wind_spd,)
print("cordinatelat:",cordinatelat,)