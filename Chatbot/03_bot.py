import pyautogui
import pyperclip
import time
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def is_last_message_from_sender(chat_log, sender_name="Aditya Kumar Gupta"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2026]")[-1]
    if sender_name not in messages:
        return True 
    return False

# Click on Brave icon to bring it into focus
pyautogui.click(227, 1050)
time.sleep(1)  # let the window come into focus

while True:
    time.sleep(5)
    # Drag to select the text region
    pyautogui.moveTo(666, 219, duration=0.2)
    pyautogui.dragTo(820, 969, duration=3.0, button="left")
    # time.sleep(3)

    # Copy the selected text
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1.5)  # give the clipboard a moment to update
    pyautogui.click(822, 969)

    # Now read what was actually just copied
    chat_history = pyperclip.paste()
    print(chat_history)

    if is_last_message_from_sender(chat_history):
        client = OpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

        completion = client.chat.completions.create(
            model="gemini-3.5-flash-lite",
            messages=[
                {"role": "system", "content": "You are a person named Aditya. Please analyze chat history and respond like Aditya and continue to chat. Aditya speaks english, hinglish and nepali similar to hinglish. For example if we say 'khana khaya?' in hinglish, we also say 'khana khayo?' in nepali. So please respond in the language used in the chat. Please dont reply with time stamp in the response. Output should be next response as Aditya on the basis of chat."},
                {"role": "user", "content": chat_history}
            ]
        )

        response = (completion.choices[0].message.content)

        pyperclip.copy(response)
        pyautogui.click(820, 969)
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.press('enter')