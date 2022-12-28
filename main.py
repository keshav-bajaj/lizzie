from modules.script import summarize, contains
from modules.workers import search, show_stats, show_archive
from modules.auth import login, sign_up, logout

logo = """ __       ______ ________ ________ ______ ________ 
|  \     |      \        \        \      \        \

| ▓▓      \▓▓▓▓▓▓\▓▓▓▓▓▓▓▓\▓▓▓▓▓▓▓▓\▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓
| ▓▓       | ▓▓     /  ▓▓    /  ▓▓  | ▓▓ | ▓▓__    
| ▓▓       | ▓▓    /  ▓▓    /  ▓▓   | ▓▓ | ▓▓  \   
| ▓▓       | ▓▓   /  ▓▓    /  ▓▓    | ▓▓ | ▓▓▓▓▓   
| ▓▓_____ _| ▓▓_ /  ▓▓___ /  ▓▓___ _| ▓▓_| ▓▓_____ 
| ▓▓     \   ▓▓ \  ▓▓    \  ▓▓    \   ▓▓ \ ▓▓     \

 \▓▓▓▓▓▓▓▓\▓▓▓▓▓▓\▓▓▓▓▓▓▓▓\▓▓▓▓▓▓▓▓\▓▓▓▓▓▓\▓▓▓▓▓▓▓▓
"""
f = contains("e", ["e"])
commands = {
    "search": "search    - to search for a topic",
    "summarize": "summarize - to summarize a huge amount of text",
    "help": "help      - to see the list of commands",
    "login": "login     - to login into your account",
    "signup": "signup    - to create a new account",
    "logout": "logout    - to logout of your account",
    "archive": "archive   - to see all your saved searches",
    "stats": "stats     - to see some stats related to your account",
    "quit": "quit      - to quit the program"
}


def display_commands():
    print("\nJust type the command you want to use\n")
    for command in commands.values():
        print(">", command)


def init():
    password = input("Root Password: ")
    if password == "keshav-ayan":
        print(logo)
        print("\nLogged In As Root\n")
        display_commands()
    else:
        print("\nIncorrect Password\n")
        init()


init()

logged_in = False
prefix = "Guest"

while True:
    command = input(prefix + " >")
    if command not in commands.keys():
        print("\n#_#\n")
    else:
        if command in list(commands.keys())[5:9]:
            if not logged_in:
                print("\nYou need to login to use these commands.\n")
            else:
                if command == "logout":
                    print()
                    (logged_in, prefix) = logout()
                elif command == "archive":
                    print()
                    show_archive(prefix)
                elif command == "stats":
                    print()
                    show_stats(prefix)
        elif command == "login":
            print()
            (logged_in, prefix) = login()
        elif command == "search":
            print()
            print(search(input("What to search? "), logged_in, prefix))
        elif command == "summarize":
            print()
            summarize("Trr")
        elif command == "help":
            print()
            display_commands()
        elif command == "signup":
            print()
            sign_up()
        elif command == "quit":
            print()
            print("\nSee you soon ~ Lizzie\n")
            break
