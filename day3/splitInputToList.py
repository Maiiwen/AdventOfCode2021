def openFileToTab():
    file = open("AdventOfCode2021\day3\input.txt", "r")
    file = file.read()
    tab = file.split("\n")
    del tab[len(tab)-1]
    return file.split("\n")
