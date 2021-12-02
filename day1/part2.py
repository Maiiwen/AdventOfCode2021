inputValues = []
increment = 0
n1 = inputValues[0] + inputValues[1] + inputValues[2]
for i in range(len(inputValues)-3):
    n2 = inputValues[i+1] + inputValues[i+2] + inputValues[i+3]
    increment += 1 if n2 > n1 else 0
    n1 = n2
print(increment)