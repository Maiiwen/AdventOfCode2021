def openFileToTab():
    bingo = []
    file = open("day4\input", "r")
    file = file.read()
    tab = file.split("\n\n")
    tirage = tab[0].split(",")
    for i in range(len(tirage)):
        tirage[i] = int(tirage[i])
    del tab[0]
    for i in range(len(tab)):
        if tab[i] != '': 
            bingo += [tab[i].split("\n")]
    
    return bingo,tirage
