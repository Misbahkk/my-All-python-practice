
# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voice', voices[1].id)


# def speak(audio):
#     # is function sa ham audio la rhe hn
#     engine.say(audio)
#     engine.runAndWait()


# def wishMe():
#     '''
#     is function ma jarvis ham ko ganton ka hisab sa wish kare ga
#     matlb ka morning or evening ka type saa
#     '''
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         speak("GoOd Morning! Misbah")
#     elif hour >= 12 and hour < 18:
#         speak("Good AfterNoon! Misbah")
#     else:
#         speak("Good Evening! Misbah")
#     speak("I am jarvis! How can i Help You Mam")


# def takeCommand():
#     # user sa voice la ga or use string ma convert kr dega
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print('Listing...')
#         r.pause_threshold = 100
#         audio = r.listen(source)
#         try:
#             print('Recognize...')
#             query = r.recognize_google(audio)
#             print("User said: " + query)
#     # agr mera jarvis sai nh sun paya to ya hoga
#         except Exception:
#             print("Plzz say again")
#             return "None"
#         return query


# if __name__ == "__main__":
#     # speak("Misbah is a good girl")
#     wishMe()
#     query = takeCommand().lower()

#     if 'wikipedia' in query:
#         speak('serching wikipedia...')
#         query = query.replace("wwikipesia", "")
#         results = wikipedia.summary(query, sentences=2)
#         speak("Accourding to wikipedia ")
#         print(results)
#         speak(results)


# wishMe()
# takeCommand()
# ==========================================================
# ==========================================================
# ==========================================================
# import speech_recognition as sr


# def check_voice(voice):
#     authorized_voices = ["Misbah Yousaf", "John Smith", "Jane Doe"]
#     if voice in authorized_voices:
#         return True
#     else:
#         return False


# if __name__ == "__main__":
#     voice = sr.Recognizer().record()
#     if check_voice(voice):
#         print("Hello, Misbah!")
#     else:
#         print("Sorry, you're not my owner.")

# import speech_recognition as sr


# def record_voice():
#     recognizer = sr.Recognizer()
#     with sr.AudioFile("C:/Users/ADMIN/Downloads/misbah.opus") as audio_file:
#         audio = recognizer.record(audio_file)
#     return audio


# def save_voice(audio):
#     with open("voice.txt", "wb") as file:
#         file.write(audio)


# if __name__ == "__main__":
#     audio = record_voice()
#     save_voice(audio)

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
