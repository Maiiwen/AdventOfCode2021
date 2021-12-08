lanternfishes = [1]
for i in range(256):
    for j in range(len(lanternfishes)):
        if lanternfishes[j] == 0:
            lanternfishes[j] = 6
            lanternfishes += [8]
        else:
            lanternfishes[j] -= 1
print(len(lanternfishes))