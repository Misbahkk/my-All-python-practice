import datetime as dt
import requests
from config import apikey


def kel_to_cel_fahre(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius *1.8+32
    return celsius , fahrenheit
city_name = "matli"
data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city_name +"&appid="+apikey).json()


temp_kelvin = data['main']['temp']
temp_celsius , temp_fahrenheit = kel_to_cel_fahre(temp_kelvin)
feels_like_kelvin = data['main']['temp']
feels_like_celsius , feels_like_fahrenheit = kel_to_cel_fahre(feels_like_kelvin)
wind_speed = data['wind']['speed']
humidity = data['main']['humidity']
description = data['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
print(f"Temprature in {city_name}  : {temp_celsius:.2f}C or {temp_fahrenheit:.2f}F")
print(f"Temprature in {city_name} feels like  : {feels_like_celsius:.2f}C or {feels_like_fahrenheit:.2f}F")
print(f"Humidity in {city_name} : {humidity}")
print(f"Wind Speed in {city_name} : {wind_speed}m/s")
print(f"Gernal Weather in {city_name} : {description}")
print(f"Sun rises in {city_name} at {sunrise_time} local time.")
print(f"Sun sets in {city_name} at {sunset_time} local time.")

