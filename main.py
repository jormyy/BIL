import time
from input_output import listen_to_command
from commands import commands
from spotify_access import get_token, authenticate


def main():
    sp = authenticate()
    token = get_token()
    
    timer = time.time()
    
    while True:
        if time.time() - timer >= 600:
            sp = authenticate()
            token = get_token()
            
        query = listen_to_command().lower()
        if "go away" in query:
            return
        if "hey bill" in query:
            query = query.replace("hey bill ", "")
            commands(query, sp, token)
        
        
if __name__ == "__main__":
    main()