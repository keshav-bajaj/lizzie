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
# def register():
#     index = 0
#     paths = ["./data/users.dat","./data/stats.dat","./data/archives/dzy.dat"]
#     baseData = [["dzy","1d506c3220b341a81721408ddfe1674629eb8ecf3d9d5a39caf18681f0cf96cc"],
#                 ["dzy",{"joined":"02/12/2022",
#                         "searches":1,
#                         "archive_size":""}],
#                 ["dzy","8letters"]
#     ]
#     for path in paths:
#         if not loadBin(path):
#             with open(path,"wb") as f:
#                 pickle.dump(baseData[index],f)
#         index += 1

usersfile = "/Users/mac/Documents/Python/csproject/data/users.dat"
# def checkAccount(user):
#     users = loadBin(usersfile)
#     print(users)
#     key = ""
#     for name in users:
#         if name[0] == user:
#             key = name[1]
#     if key == "":
#         return False
#     else:
#         return key
# print(checkAccount("dzy"))

print(loadBin(usersfile))