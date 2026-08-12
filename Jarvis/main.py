import os
from dotenv import load_dotenv
from contextlib import contextmanager
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import musicLibrary
from openai import OpenAI
from gtts import gTTS
import pygame
import subprocess

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
base_dir = os.getenv("base_dir")

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

# Function to return script path (pass script name without .sh)
def get_script_path(scriptname):
    script_path = os.path.join(base_dir, "scripts", f"{scriptname}.sh")
    return script_path

# Function to return file path (pass file's name without .txt)
def get_file_path_to_read_content(filename):
    file_path = os.path.join(base_dir, "tmp", f"{filename}.txt")
    return file_path

# Function to read data from file (pass file's whole directory via argument)
def read_data(filepath):
    with open(filepath, "r") as f:
        data = f.read().strip() 
    return data 

# Function to read lines 
def read_lines(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    return lines

def ask_file_name():
    script = get_script_path("ask_file_name")
    # speak("Enter the name of the file or folder you want to delete, starting with")
    subprocess.Popen(["gnome-terminal", "--wait", "--", "bash", "-c", f'"{script}"; sleep 0.25']).wait()
    file = get_file_path_to_read_content("filename")
    content = read_data(file)
    return content

def file_deletion():

    file_content = ask_file_name() # stores file's name to delete
    script = get_script_path("find_files_or_folders")
    subprocess.Popen(["gnome-terminal", "--wait", "--", "bash", "-c", f'"{script}" "{file_content}"']).wait()
    count_file = get_file_path_to_read_content("count")
    count = (read_data(count_file))
    # speak(f"{count} results found.")
    print(f"{count} results found.")

    if int(count) > 0:
        # speak(f"Shall {count} results be deleted? ")
        ans = input(f"Shall {count} results be deleted? ")

        if "yes" in ans.lower():
            # speak(f"How the results should get deleted? In one go or one by one?")
            deletion_way = input("How the results should get deleted? \n (In one go: 1) \n (One by one: 2) \n Please choose: ")
            
            # if "in one go" in deletion_way.lower():
            if int(deletion_way) == 1:
                # speak(f"Proceed to delete {count} results in one go? (yes/no)")
                ans1 = input(f"Proceed to delete {count} results in one go? (yes/no): ")

                if "yes" in ans1.lower(): 
                    script = get_script_path("delete1_in_one_go")
                    file_path = get_file_path_to_read_content("filename")
                    file_content = read_data(file_path)
                    subprocess.Popen(["gnome-terminal", "--wait", "--", "bash", "-c", f'"{script}" "{file_content}"; sleep 0.5']).wait()
                    file_path_of_count_of_diog = get_file_path_to_read_content("count_of_diog")
                    content_of_count_of_diog = read_data(file_path_of_count_of_diog) 
                    # speak(f"{content_of_count_of_deletion_in_one_go} results deleted.")
                    print(f"{content_of_count_of_diog} results deleted.")
                elif "no" in ans1.lower():
                    # speak(f"Deletion stopped.")
                    print(f"Deletion stopped.")
                else:
                    # speak("Command unclear. Deletion stopped.")
                    print("Command unclear. Deletion stopped.")

            elif int(deletion_way) == 2:
                # speak(f"Proceed to delete {count} results one by one? (yes/no)")
                ans1 = input(f"Proceed to delete {count} results one by one? (yes/no): ")


                if "yes" in ans1.lower(): 
                    count1 = 0
                    while True:                        
                        file_path = get_file_path_to_read_content("found_files")
                        data_lines = read_lines(file_path)
                        print(f"List of files: {data_lines}")
                        for file in data_lines:
                            # first_line = data_lines[0]
                            base_name = os.path.basename(file)
                            # speak(f"{base_name} should be deleted? ") 
                            ans2 = input(f"{base_name} should be deleted? ") 

                            if "yes" in ans2.lower():
                                script = get_script_path("delete_one_file_or_folder")                            
                                subprocess.Popen(["gnome-terminal", "--wait", "--", "bash", "-c", f'"{script}" "{file}"; sleep 0.5']).wait()
                                # subprocess.run([script, file])
                                count1 += 1
                                # script = get_script_path("find_files_or_folders")
                                # file_content1 = read_data("filename")
                                # subprocess.Popen(["gnome-terminal", "--wait", "--", "bash", "-c", f'"{script}" "{file_content1}"']).wait()                            
                                # speak(f"{base_name} deleted.")
                                print(f"{base_name} deleted.")
                            elif "no" in ans2.lower():
                                # speak(f"Skipped {base_name}")
                                print(f"Skipped {base_name}.")
                            elif "stop" in ans2.lower():
                                # speak(f"Deletion stopped.")
                                print(f"Deletion stopped.")
                                break
                            else :
                                # speak("Command unclear. Deletion stopped.")
                                print("Command unclear. Deletion stopped.")
                                break
                        # speak(f"{count1} results deleted.")
                        print(f"{count1} results deleted.")
                        # speak(f"Remaining results: {count-count1}")
                        print(f"Remaining results: {int(count)-count1}")
                        script = get_script_path("find_files_or_folders")
                        file_nam = get_file_path_to_read_content("filename")
                        file_name = read_data(file_nam)
                        subprocess.Popen(["gnome-terminal", "--wait", "--", "bash", "-c", f'"{script}" "{file_name}"; sleep 0.5']).wait()
                elif "no" in ans1.lower():
                    # speak(f"Deletion stopped.")
                    print(f"Deletion stopped.")
                else:
                    # speak("Command unclear. Deletion stopped.")
                    print("Command unclear. Deletion stopped.")
            else:
                # speak("Command unclear. Deletion stopped.")
                print("Command unclear. Deletion stopped.")
        elif "no" in ans1.lower():
            # speak(f"Deletion stopped.")
            print(f"Deletion stopped.")
        else:
            # speak("Command unclear. Deletion stopped.")
            print("Command unclear. Deletion stopped.")       
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open brave" in c.lower():
        subprocess.Popen(["brave-browser"])
    elif "open chrome" in c.lower():
        subprocess.Popen(["google-chrome"])
    elif "open intelli j" in c.lower():
        subprocess.Popen(["intellij-idea-ultimate"])
    elif "remove" in c.lower():
        file_deletion()
        # subprocess.Popen(["gnome-terminal", "--", "bash", "-c", "./scripts/deletion_script.sh; sleep 1"])
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
                # speak(article['title'])
                print(article['title'])
    else:
        # Let openai handle the request
        speak(aiProcess(c))
    

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    file_deletion()
    # while True:
    #     r = sr.Recognizer()

    #     try:
    #         with suppress_stderr():
    #             with sr.Microphone() as source:
    #                 print("Listening...")
    #                 audio = r.listen(source, timeout=10, phrase_time_limit=10)
    #             word = r.recognize_google(audio)
    #             if ("jarvis" in word.lower()):
    #                 speak("Yeah")
    #                 # Listen for command
    #                 with sr.Microphone() as source:
    #                     print("Jarvis Active...")
    #                     # Audio input
    #                     audio = r.listen(source) # Human speech stored in audio
    #                     # Speech to text 
    #                     command = r.recognize_google(audio) # Human speech into text and stored in command

    #                     processCommand(command) # Sending text form of human speech as argument

    #     except Exception as e:
    #         print("Recognition error: {0}".format(e))