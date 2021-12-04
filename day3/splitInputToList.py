def openFileToTab():
    file = open("day3\input.txt", "r")
    file = file.read()
    tab = file.split("\n")
    del tab[len(tab)-1]
    for i in range(len(tab)):
        tab[i] = str(tab[i])
    return file.split("\n")
