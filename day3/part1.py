from splitInputToList import openFileToTab
inputValues = openFileToTab()
del inputValues[(len(inputValues)-1)]
lenValues = len(inputValues)
count = [0] * len(inputValues[0])
gamma = [0] * len(inputValues[0])
epsilon = [0] * len(inputValues[0])
for i in range(len(inputValues)):
    entry = str(inputValues[i])
    for i in range(len(entry)):
        if entry[i] == "1":
            count[i] += 1
for i in range(len(entry)):
    gamma[i] = 1 if count[i] > (lenValues//2) else 0 
    epsilon[i] = 0 if count[i] > (lenValues//2) else 1

print(count)
print(gamma,epsilon)
