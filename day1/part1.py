inputValues = []
increment = 0
n1 = inputValues[0]
for i in range(len(inputValues)-1):
    n2 = inputValues[i+1]
    increment += 1 if n2 > n1 else 0
    n1 = n2
print(increment)