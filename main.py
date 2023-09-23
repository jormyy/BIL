from input_output import listen_to_command
from commands import commands


def main():
    
    while True:
        query = listen_to_command().lower()
        if "go away" in query:
            return
        if "hey bill" in query:
            query = query.replace("hey bill ", "")
            commands(query)
        
        
if __name__ == "__main__":
    main()