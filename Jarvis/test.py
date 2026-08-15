import os
from contextlib import contextmanager
import speech_recognition as sr

r = sr.Recognizer()

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

def speech_to_text():
    max_retries = 3
    for attempt in range(max_retries):
        try:
            with suppress_stderr():
                with sr.Microphone() as source:
                    audio1 = r.listen(source, timeout=5, phrase_time_limit=5)
                    command1 = r.recognize_google(audio1)
                    print(command1)
                    return command1
        except sr.UnknownValueError:
            print("Didn't catch that, try again...") 
        except Exception as e:
            print(f"Recognition error: {e}")
    return ""  # give up after retries


speech_to_text()
