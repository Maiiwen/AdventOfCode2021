from splitInputToList import openFileToTab
inputValues = openFileToTab()
lenValues = len(inputValues)
count = [0] * len(inputValues[0])
gamma = ""
epsilon = ""
for i in range(len(inputValues)):
    entry = str(inputValues[i])
    for j in range(len(entry)):
        if entry[j] == "1":
            count[j] += 1
for i in range(len(entry)):
    gamma += "1" if count[i] > (lenValues//2) else "0" 
    epsilon += "0" if count[i] > (lenValues//2) else "1"


print(int(gamma,2),int(epsilon,2))
print(int(gamma,2)*int(epsilon,2))
