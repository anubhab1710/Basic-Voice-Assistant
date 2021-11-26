import webbrowser
from time import *
import speech_recognition as sr

r = sr.Recognizer()

def record_audio(ask = False):
 with sr.Microphone() as source:
    if ask:
         print("Ask my lord")
    audio = r.listen(source)
    voice_data = ''
    try:
        voice_data = r.recognize_google(audio)
        print(voice_data)
    except sr.UnknownValueError:
        print("Sorry OWO, Didn't Hear that!!")
    except sr.RequestError:
        print("Sorry, my voice is choked")
    return voice_data 

def respond(voice_data):
    if "what is your name" in voice_data:
        print("My name is Hikari")
    if "what time is it" in voice_data:
        print(ctime())
    if "search" in voice_data:
        search = record_audio("What do you want to know senpai?")   
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open_new_tab(url)
        print("Here is what I found for " + search)
    if "find location" in voice_data:
        location = record_audio("What is the place you are looking for, baka?")   
        url = 'https://google.com/maps/place/' + location 
        webbrowser.get().open_new_tab(url)
        print("Here is what I found for " + location)
    if "exit" in voice_data:
        exit()    

#time.sleep(1)
print("How can I help you senpai")
while(1):
    voice_data = record_audio()
    respond(voice_data)
