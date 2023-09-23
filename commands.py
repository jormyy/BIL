import datetime
import pywhatkit as pwk
from input_output import talk


def commands(instruction):
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