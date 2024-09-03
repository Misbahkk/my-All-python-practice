#API_KEY = '40f37c911820e9f79b38ca25c98f6815'
city_name = "Karachi"
data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city_name +"&appid="+API_KEY)
print(data)
