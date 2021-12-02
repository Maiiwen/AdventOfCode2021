inputValues = []
x, y,aim = 0,0,0
for i in range(len(inputValues)):
    if "up" == inputValues[i].split()[0]:
        aim -= int(inputValues[i].split()[1])
    elif "down" == inputValues[i].split()[0]:
        aim += int(inputValues[i].split()[1])
    elif "forward" == inputValues[i].split()[0]:
        y += int(inputValues[i].split()[1])
        if aim!=0:
            x += int(inputValues[i].split()[1])*aim
print(abs(x)*abs(y))

