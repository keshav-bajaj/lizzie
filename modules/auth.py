import hashlib
import pickle
from .workers import loadBin

usersfile = "./data/users.dat"
username = ""
password = ""


def prompt():
    global username
    global password

    username = input("Username: ").strip()
    password = hashlib.sha256(input("Password: ").encode("utf-8")).hexdigest()


def checkAccount(user):
    users = loadBin(usersfile)
    key = ""
    for name in users:
        if name[0] == user:
            key = name[1]
    if key == "":
        return False
    else:
        return key


def login():
    prompt()
    check = checkAccount(username)
    if not check:
        print("\nPlease register yourself first.\n")
        return (False, "Guest")
    else:
        if check == password:
            print("\nLogged In")
            return (True, username)
        else:
            print("\nWrong Password")
            return (False, "Guest")


def logout():
    username = ""
    password = ""
    return (False, "Guest")


def sign_up():
    prompt()

    global username
    global password

    users = loadBin(usersfile)
    usernames = [i[0] for i in users]
    while username in usernames:
        print("\nUsername taken\n")
        username = input("Username: ").strip()
    confirm = hashlib.sha256(input("Confirm Password: ").encode("utf-8")).hexdigest()
    while confirm != password:
        confirm = hashlib.sha256(input("Confirm Password: ").encode("utf-8")).hexdigest()
    with open(usersfile, "ab") as f:
        pickle.dump([username, password], f)
    with open(f"./data/archives/{username}.dat", "wb") as f:
        pass
    print("\nAccount Created")