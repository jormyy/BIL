import time
from input_output import listen_to_command
from commands import commands
from spotify_access import get_token, authenticate


def main():
    sp = authenticate()
    token = get_token()
    
    ten_min_timer = time.time()
    hour_timer = time.time()
    
    while True:
        if time.time() - ten_min_timer >= 600:
            sp = authenticate()
            ten_min_timer = time.time()
        if time.time() - hour_timer >= 3600:
            token = get_token()
            hour_timer = time.time()
            
        query = listen_to_command().lower()
        print(query)
        if "go away" in query:
            return
        if "bill" in query:
            query = query.replace("bill ", "")
            commands(query, sp, token)
        
        
if __name__ == "__main__":
    main()