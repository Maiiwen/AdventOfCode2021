inputValues = []
x, y = [],[]
x += [int(inputValues[i].split()[1]) for i in range(len(inputValues)) if "up" == inputValues[i].split()[0]]
x += [-int(inputValues[i].split()[1]) for i in range(len(inputValues)) if "down" == inputValues[i].split()[0]]
y += [int(inputValues[i].split()[1]) for i in range(len(inputValues)) if "forward" == inputValues[i].split()[0]]
print(abs(sum(x))*sum(y))