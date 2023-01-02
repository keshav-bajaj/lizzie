import os
os.chdir('./')

import pickle, socket
from modules.script import publish

def connected():
    try:
        s = socket.socket()
        s.connect(('google.com', 443))
        s.close()
        return True
    except:
        return False


def loadBin(filename, entries=True):
    data = []
    try:
        with open(filename, "rb") as f:
            data = []
            if not entries:
                try:
                    while entries:
                        data.append(pickle.load(f))
                        entries -= 1
                except:
                    pass
            else:
                try:
                    while True:
                        data.append(pickle.load(f))
                except:
                    pass

    except:
        return False
    return data


def search(value, logged, username):
    if logged:
        archives = loadBin(f"./data/archives/{username}.dat")
        found = False
        for archive in archives:
            if archive[0] == value:
                found = True
                print()
                return archive[1]
        if not found:
            if not connected():
                print("You are not connected to Internet and there is nothing in archive.")
            else:
                res = publish(value)
                if res != "I cannot find anything for you":
                    add_archive(username, res[1], res[0])

    else:
        res = publish(value)
        if type(res) == "list":
            return res[0]
        else:
            return res


def update_stats(username):
    pass


def show_archive(username):
    archives = loadBin(f"data/archives/{username}.dat")
    indexes = []
    index = 0
    for archive in archives:
        print(f"{index}. {archive[0]}")
        indexes.append(str(index))
        index += 1

    n = input("Type the serial number to open any: ")

    if n in indexes:
        print(f"\n{archives[int(n)][0]}")
        print("_"*(len(archives[int(n)][0]) + 5))
        print(f"{archives[int(n)][1]}")


def show_stats():
    pass


def add_archive(username, key, value):
    with open(f"./data/archives/{username}.dat", "ab") as f:
        pickle.dump([key, value], f)