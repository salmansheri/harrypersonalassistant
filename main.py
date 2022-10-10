# importing the date and time 
import datetime
# importing  pyttsx3 
import pyttsx3 as aud 
# importing speech recognition
import speech_recognition as sr
# importing pyaudio  
import pyaudio
# importing wikipedia
import wikipedia
# importing webbrowser module 
import webbrowser as wb
# importing os module 
import os
# importing smtplib module  
import smtplib
# declaration of variables 
engine = aud.init("sapi5")
# declaration of variables 
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("voices", voices[0].id)
print(voices[1].id)

# Defining the function to speak 
def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

# defining the function to wish 
def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning, Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon, sir")

    speak("I am Harry, your assistant")
    speak("How can I help you")


# listening function 
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

# defining function for sending the mail 
def sendemail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail", "password")
    server.sendmail("sheriffsalman00@gmail.com", to, content)
    server.close()

# main function 
if __name__ == '__main__':
    wishme()
    while True:
        query = listen().lower()
        # if query is wikipedia then execute this: 
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            print("Searching...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        # else if query is open youtube execute this: 
        elif "open youtube" in query:
            wb.open("www.youtube.com")

        # else if query is open google execute this: 
        elif "open google" in query:
            wb.open("www.google.com")

        # else if query is open stack overflow execute this: 
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        # else if query is "what is the time now" execute this: 
        elif "what is the time now" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("sir, the time is {}".format(strtime))
            print(strtime)

        # else if query is 'open code' execute this: 
        elif "open code" in query:
            path = "C:\\Users\\MS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        # else if query is "play music" execute this: 
        elif "play music" in query: 
            spotifypath = "C:\\Users\\MS\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifypath)

        
        # else if query is "vikram title song" execute this: 
        elif "vikram title song" in query:
            songpath = "https://www.youtube.com/watch?v=OG13_L7Iims"
            wb.open(songpath)

        # else if query is "open chrome" execute this:  
        elif "open chrome" in query:
            apppath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(apppath)

        # else if query is "salman" execute this: 
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
