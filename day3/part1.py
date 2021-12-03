from splitInputToList import openFileToTab
inputValues = openFileToTab()
del inputValues[(len(inputValues)-1)]
print(inputValues)
count = [0] * 12
for i in range(len(inputValues)):
    entry = str(inputValues[i])
    for i in range(len(entry)):
        if entry[i] == "1":
            count[i] += 1

print(count)
