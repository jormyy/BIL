import datetime
import pywhatkit as pwk
import webbrowser
from input_output import talk
from spotify_access import get_token, search_song, authenticate


urls = {
    "youtube": "https://youtube.com"
}

month_convert = {
    1: "january", 2: "february", 3: "march", 4: "april",
    5: "may", 6: "june", 7: "july", 8: "august",
    9: "september", 10: "october", 11: "november", 12: "december"
}


def commands(instruction, sp, token):
    if "play" in instruction:
        song = instruction.replace("play ", "")
        song_uri = search_song(token, song)
        sp.start_playback(uris=[song_uri])
    elif "pause" in instruction:
        sp.pause_playback() 
    elif "resume" in instruction:
        sp.start_playback()
    elif "time" in instruction:
        time = datetime.datetime.now().strftime("%I:%M%p")
        talk(f"the time is {time}")
    elif "date" in instruction:
        month = month_convert[int(datetime.datetime.now().strftime("%m"))]
        day_year = datetime.datetime.now().strftime(f"%d %Y")
        talk(f"the date is {month} {day_year}")
    elif "open" in instruction:
        if "loyal listener" in instruction:
            webbrowser.open("https://jorm.pythonanywhere.com")
        elif "youtube" in instruction:
            webbrowser.open(urls["youtube"])