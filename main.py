import pyttsx3
import speech_recognition as sr
import datetime
import random
import wikipedia
import webbrowser
import os
import time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def mic_input():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

        try:
            print("Reading Voice...")
            query = r.recognize_google(audio, language='en-in')
            print(f"Query: {query}\n")

        except Exception as e:
            print(e)
            print("Please Repeat...")
            return "No Audio"
        return query

def wish():
    morning=["Good Morning Sir","A very good morning sir","Merry Morning"]
    noon=['Good Noon',"Good Noon Sir",'Noon sir']
    afternoon=["Good afternoon","good afternoon sir","afternoon sir"]
    evening=["good evening","good evening sir","evening sir","evening"]
    night=["Good night sir","Good night","Night sir","Merry dreams sir"]
    day_hour=int(datetime.datetime.now().hour)
    if day_hour>=4 and day_hour<12:
        speak(random.choise(morning))
    elif day_hour==12:
        speak(random.choice(noon))
    elif day_hour>12 and day_hour<=17:
        speak(random.choice(afternoon))
    elif (day_hour>17 and day_hour<24) or (day_hour>=0) :
        speak(random.choice(evening))

if __name__=="__main__" :
    wish()
    while True:
        stat=1
        query = mic_input().lower()
        print(query)

        if 'lock query' in query:
            stat=0
            speak("Locked Speech Input")

        if 'unlock query' in query:
            if stat==0:
                speak("Input Password")
                pwd=mic_input()
                pwd=pwd.lower()
                if pwd=='rainy day':
                    stat=1
                    speak("Query Unlocked")
                else :
                    speak("Password incorrect")


        if 'search' in query:
            if stat ==1:
                speak('Looking up Wikipedia...')
                query = query.replace("search", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia ")
                print(results)
                speak(results)
            else :
                speak("Query Locked")

        if 'youtube' in query:
            if stat==1:
                webbrowser.open("youtube.com")
            else:
                speak("Query Locked")

        if 'google' in query:
            if stat==1:
                webbrowser.open("google.com")
            else:
                speak("Query Locked")

        if 'atom' in query:
            code_path = 'C:\\Users\\Me\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\GitHub, Inc\\Atom'
            if stat==1:
                os.startfile(code_path)
            else:
                speak("Query Locked")

        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        if 'exit' in query:
            speak("Closing all instances")
            exit()

        if 'timer' or 'reminder':
            speak("Timer Set")
            time.sleep(int(query[-10:-9]))
            speak("Ping Ping Ping")
