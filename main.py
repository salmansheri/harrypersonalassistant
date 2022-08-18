import datetime

import pyttsx3 as aud
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser as wb
import os
import smtplib



engine = aud.init("sapi5")
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("voices", voices[0].id)
print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning, Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon, sir")

    speak("I am Harry, your assistant")
    speak("How can I help you")


def listen():
    """
    It takes microphone input
    :return: String output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing sir")
        query = r.recognize_google(audio, language="en-in")
        print("User said: {}\n".format(query))

    except Exception as e:
        print(e)
        print("Say that again sir Please...")
        speak("Sorry sir I cannot understand please say that again sir")

        return "None"

    return query


def sendemail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail", "password")
    server.sendmail("sheriffsalman00@gmail.com", to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    while True:
        query = listen().lower()
        # Logic to execute the task
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            print("Searching...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            wb.open("www.youtube.com")

        elif "open google" in query:
            wb.open("www.google.com")

        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "what is the time now" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("sir, the time is {}".format(strtime))
            print(strtime)
        elif "open code" in query:
            path = "C:\\Users\\MS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif "play music" in query:
            spotifypath = "C:\\Users\\MS\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifypath)

        elif "vikram title song" in query:
            songpath = "https://www.youtube.com/watch?v=OG13_L7Iims"
            wb.open(songpath)

        elif "open chrome" in query:
            apppath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(apppath)

        elif "salman" in query:
            try:
                speak("What should i say")
                content = listen()
                to = "sheriffsalman00@gmail.com"
                sendemail(to, content)
                speak("Email has been sent")
                print("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this Email, please try again ")
