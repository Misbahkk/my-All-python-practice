# import speech_recognition as sr
# import win32com.client
# import os


# def say(text):
#     speak = win32com.client.Dispatch("SAPI.SpVoice")
#     speak.Speak(text)


# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.pause_threshold = 1
#         audio = r.listen(source)

#         query = r.recognize_google(audio, language="en-in")
#         print(f"User Said:{query}")
#         return query


# if __name__ == '__main__':
#     print('Pycharm')
#     say("Hello I am Jarvis A I")
#     print("listening....")
#     text = takeCommand()
#     say(text)

import speech_recognition as sr


def check_voice(voice):
    authorized_voices = ["Misbah Yousaf", "John Smith", "Jane Doe"]
    if voice in authorized_voices:
        return True
    else:
        return False


if __name__ == "__main__":
    with sr.Microphone() as source:
        print("listing....")
        voice = sr.Recognizer().record(source)

    if check_voice(voice):
        print("Hello, Misbah!")
    else:
        print("Sorry, you're not my owner.")
