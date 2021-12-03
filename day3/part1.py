import sys
sys.path.append('../')
from splitInputToList import openFileToTab
inputValues = openFileToTab()
count = [0]*len(inputValues[0])
for i in range(len(inputValues)):
    inputValues[i] = list(str(inputValues[i]))
print(inputValues)
for i in range(len(count)):
    for j in range(len(inputValues)):
        count[i] += 1 if inputValues[i][j] == "1" else 0
print(count)
