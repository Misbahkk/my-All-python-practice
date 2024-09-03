import speech_recognition as sr
# import win32com.client
import os
import webbrowser
import openai
from config import apikey
from config import weather_apikey
import datetime as dt
import requests
import pyttsx3

# Introduce Yourselfs
# def intro():
#     openai.api_key = apikey
#     intro_Q = "Can you tell me about yourself in short manner and eassy words , abby? What are the things you can do? I've created you to represent me in my class. You have some features like opening websites like YouTube and other sites. When I say 'using AI,' you create a directory called 'openai' and save responses in files. You can open songs, tell the current time, provide weather information, and even chat like a friend. I've also incorporated voice recognition, so when someone says 'abby, quit,' you shut down. Can you explain all this in a way that's easy to understand and short time ? "

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "user", "content": intro_Q}
#         ],
#         temperature=0.5,
#         max_tokens=150,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     message_content = response["choices"][0]["message"]["content"]
#     say(message_content)
#     intro_Q += f"{message_content}\n"
#     print(intro_Q)
#     return message_content


# find the weather using API
def kel_to_cel_fahre(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * 1.8+32
    return celsius, fahrenheit


def weather_info(city):
    # city_name = "matli"
   # data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" +
          #              city + "&appid="+weather_apikey).json()

    temp_kelvin = data['main']['temp']
    temp_celsius, temp_fahrenheit = kel_to_cel_fahre(temp_kelvin)
    feels_like_kelvin = data['main']['temp']
    feels_like_celsius, feels_like_fahrenheit = kel_to_cel_fahre(
        feels_like_kelvin)
    # wind_speed = data['wind']['speed']
    # humidity = data['main']['humidity']
    # description = data['weather'][0]['description']
    # sunrise_time = dt.datetime.utcfromtimestamp(
    #     data['sys']['sunrise'] + data['timezone'])
    # sunset_time = dt.datetime.utcfromtimestamp(
    #     data['sys']['sunset'] + data['timezone'])
    say(f"Temprature in {city}  : {temp_celsius:.2f}C or {temp_fahrenheit:.2f}F")
    print(
        f"Temprature in {city} feels like  : {feels_like_celsius:.2f}C or {feels_like_fahrenheit:.2f}F")
    # print(f"Humidity in {city} : {humidity}")
    # print(f"Wind Speed in {city} : {wind_speed}m/s")
    # print(f"Gernal Weather in {city} : {description}")
    # print(f"Sun rises in {city} at {sunrise_time} local time.")
    # print(f"Sun sets in {city} at {sunset_time} local time.")


# Chat with abby like a chatgpt
chatStr = ""


def chat(query):
    global chatStr
    openai.api_key = apikey
    if "introduce yourself".lower() in query.lower():
        chatStr += "Can you tell me about yourself in short manner and eassy words , abby? What are the things you can do? I am misbah Yousaf. I've created you to represent me in my class.You are my virtual desktop assisten. You have some features like opening websites like YouTube and other sites. When I say 'using AI,' you create a directory called 'openai' and save responses in files. You can open songs, tell the current time, provide weather information, and even chat like a friend. I've also incorporated voice recognition, so when someone says 'abby, quit,' you shut down. Can you explain all this in a way that's easy to understand and short time ? "

    else:
        chatStr += f"Misabh : {query}\n abby : "

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": chatStr}
        ],
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    message_content = response["choices"][0]["message"]["content"]
    say(message_content)
    chatStr += f"{message_content}\n"
    print(chatStr)
    return message_content


# when user day using ai then this part do work and crete another file and save date
def ai(message):
    openai.api_key = apikey
    text = f"OpenIA response for Message : {message} \n*************************\n\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ],
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    message_content = response["choices"][0]["message"]["content"]
    # print(message_content)
    text += message_content
    if not os.path.exists("openai"):
        os.mkdir("openai")
    with open(f"openai/{''.join(message.split('AI')[1:]).strip()}.txt", "w") as f:
        f.write(text)


# say funtion
# Initialize the engine and get available voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)  # Adjust the rate as needed


def say(text):
    engine.say(text)
    engine.runAndWait()
    # speak = win32com.client.Dispatch("SAPI.SpVoice")
    # speak.Speak(text)


def wishMe():
    '''
    is function ma abby ham ko ganton ka hisab sa wish kare ga
    matlb ka morning or evening ka type saa
    '''
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say("GoOd Morning! Misbah Yousaf")
    elif hour >= 12 and hour < 18:
        say("Good AfterNoon! Misbah Yousad")
    else:
        say("Good Evening! Misbah Yousaf")
    say("I am abby! How can i Help You Mam")


# Take a command from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("regonition......")
            query = r.recognize_google(audio, language="en-pk")
            print(f"User Said:{query}")
            return query
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand what you said."
        except sr.RequestError:
            return "Sorry, there was an error connecting to the speech recognition service."
        except Exception as e:
            return "SOme Error Occurred. Sorry from abby"

if __name__ == '__main__':
    wishMe()
    while True:
        print("listening....")
        query = takeCommand()
        if "open" in query:
            sites = [["youtube", "https://youtube.com"], ["googel", "https://googel.com"],
                     ["wikipedia", "https://wikipedia.com"], ["facebook", "https://facebook.com"],]
            for site in sites:
                if f"Open {site[0]}".lower() in query.lower():
                    say(f" Opening {site[0]} Mam....")
                    webbrowser.open(site[1])
        elif "open music" in query:
            musicPath = "C:/Users/ADMIN/Downloads/downfall-21371.mp3"
            os.startfile(musicPath)
        elif "the time" in query:
            hour = dt.datetime.now().strftime("%H")
            min = dt.datetime.now().strftime("%M")
            say(f"Mam time is {hour} and {min} minutes")

        elif "Using AI".lower() in query.lower():
            ai(message=query)
        elif "weather".lower() in query.lower():
            cities = [" Faisalabad", " Lahore", " Islamabad", "Karachi",
                      "Matli", "Jamshoro", "University Of Sindh Jamshoro", "Hyderabad"]
            city = None
            for user_city in cities:
                if user_city.lower() in query.lower():
                    city = user_city
                    break
            if city:
                weather_info(city)
            else:
                say("Sorry, I couldn't recognize the city name in your query.")
        elif "abby Quit".lower() in query.lower():
            exit()
        elif "Reset the chat".lower() in query.lower():
            chatStr = ""
        # elif "introduce yourself".lower() in query.lower():
        #     intro()
        else:
            chat(query)
