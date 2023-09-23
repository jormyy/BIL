import datetime
import webbrowser
from input_output import talk
from spotify_access import search_song


urls = {
    "youtube": "https://youtube.com",
    "canvas": "https://canvas.ucdavis.edu",
    "github": "https://github.com",
    "linkedin": "https://www.linkedin.com/in/jeremy1112ha/",
    "gmail": "https://mail.google.com/mail/u/0/#inbox"
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
            talk("opening loyal listener")
            
        elif "youtube" in instruction:
            webbrowser.open(urls["youtube"])
            talk("opening youtube")
            
        elif "canvas" in instruction:
            webbrowser.open(urls["canvas"])
            talk("opening canvas")
            
        elif "github" in instruction:
            webbrowser.open(urls["github"])
            talk("opening git hub")
            
        elif "linkedin" in instruction:
            webbrowser.open(urls["linkedin"])
            talk("opening linkedin")
            
        elif "gmail" in instruction:
            webbrowser.open(urls["gmail"])
            talk("opening gmail")