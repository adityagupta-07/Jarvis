# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# if __name__ == "__main__":
#     speak("Initializing Jarvis...")
#     while True:
#         # listen for the wake word "Jarvis":
#         # obtain audio from the microphone
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             print("Listening...") 
#             audio = r.listen(source)

#         print("recognizing...")
#         try:
#             command = r.recognize_google(audio)
#             print(command)
#         except sr.UnknownValueError:
#             print("Sphinx could not understand audio")
#         except sr.RequestError as e:
#             print("Sphinx error; {0}".format(e))

import os
from dotenv import load_dotenv
from contextlib import contextmanager
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame

@contextmanager
def suppress_stderr():
    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)
    os.dup2(devnull, 2)
    try:
        yield
    finally:
        os.dup2(old_stderr, 2)
        os.close(devnull)
        os.close(old_stderr)

load_dotenv()
# recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "6d136bfb15f8484392d9c9b790e5db3d"
gemini_api_key = os.getenv("GEMINI_API_KEY")

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(
        api_key= gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    completion = client.chat.completions.create(
        model="gemini-3.5-flash-lite",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Please respond in plain text with no any text formatting. Please also give short responses."},
            {"role": "user", "content": command}
        ]
    )

    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parese the json response    
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                speak(article['title'])
    else:
        # Let openai handle the request
        speak(aiProcess(c))



    

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()

        try:
            with suppress_stderr():
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                word = r.recognize_google(audio)
                if ("jarvis" in word.lower()):
                    speak("Yeah")
                    # Listen for command
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)
                        

        except Exception as e:
            print("Recognition error: {0}".format(e))