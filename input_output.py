import speech_recognition as sr
import pyttsx3


def listen_to_command():
    
    listener = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        
        listener.pause_threshold = 0.5
        audio = listener.listen(source)
        
        try:
            query = listener.recognize_google(audio)
        
        except:
            return "None"

    return query


def talk(text):
    
    machine = pyttsx3.init()
    
    voices = machine.getProperty("voices")
    
    machine.setProperty("voice", voices[1].id)
    
    machine.say(text)
    
    machine.runAndWait()