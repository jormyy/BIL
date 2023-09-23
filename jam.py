import speech_recognition as sr
import pyttsx3
import pywhatkit as pwk
import datetime


listener = sr.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()


def input_instruction():
    with sr.Microphone() as origin:
        print("listening")
        while True:
            try:
                speech = listener.listen(origin)
                instruction = listener.recognize_google(speech).lower()
                if "hello" in instruction:
                    instruction = instruction.replace("hello", "")
                    break
            except sr.WaitTimeoutError:
                continue
    return instruction
    

def play_jam():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace("play", "")
        talk(f"playing {song}")
        pwk.playonyt(song)
    elif "time" in instruction:
        time = datetime.datetime.now().strftime("%I:%M%p")
        talk(f"the time is {time}")
    elif "date" in instruction:
        date = datetime.datetime.now().strftime("%m / %d / %Y")
        talk(f"the date is {date}")
    
    
while True:
    try:
        play_jam()
    except sr.WaitTimeoutError:
        continue