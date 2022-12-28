import hashlib
import pickle
from datetime import date
from .workers import loadBin

usersfile = "/Users/mac/Documents/Python/csproject/data/users.dat"
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
            print("\nLogged In\n")
            return (True, username)
        else:
            print("\nWrong Password\n")
            return (False, "Guest")


def logout():
    username = ""
    password = ""
    return (False, "Guest")


def sign_up():
    prompt()

    global username
    global password

    users = loadBin("/Users/mac/Documents/Python/csproject/data/users.dat")
    usernames = [i[0] for i in users]
    while username in usernames:
        print("\nUsername taken\n")
        username = input("Username: ").strip()
    confirm = hashlib.sha256(input("Confirm Password: ").encode("utf-8")).hexdigest()
    while confirm != password:
        confirm = hashlib.sha256(input("Confirm Password: ").encode("utf-8")).hexdigest()
    with open("/Users/mac/Documents/Python/csproject/data/users.dat", "ab") as f:
        pickle.dump([username, password], f)
    with open(f"/Users/mac/Documents/Python/csproject/data/archives/{username}.dat", "wb") as f:
        pass
    # with open(f"../data/stats.dat", "wb") as f:
    #     pickle.dump([username, {"joined": date.today().strftime("%d/%m/%Y"),
    #                             "searches": 0,
    #                             "archive_size": 0}], f)
    print("\nAccount Created\n")

# with open(usersfile,"wb") as f:
#     pickle.dump(["dzy","1d506c3220b341a81721408ddfe1674629eb8ecf3d9d5a39caf18681f0cf96cc"],f)
