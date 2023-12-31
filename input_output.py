import speech_recognition as sr
import pyttsx3


MAX_DURATION = 4

def listen_to_command():
    
    listener = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        
        listener.pause_threshold = 0.7
        listener.adjust_for_ambient_noise(source)
        
        try:
            audio = listener.listen(source, timeout=MAX_DURATION)
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