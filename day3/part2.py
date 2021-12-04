from splitInputToList import openFileToTab
inputValues = openFileToTab()
def number(inputValues,var):
    for i in range(len(inputValues[0])):
        ones, zeros = [],[]
        for j in range(len(inputValues)):
            entry = inputValues[j]
            if entry[i] == "1": ones += [entry] 
            else: zeros += [entry]
        if var == "co2":
            inputValues = zeros if  len(ones) >= len(zeros) else ones
        if var == "oxygen":
            inputValues = zeros if  len(ones) < len(zeros) and len(zeros) != len(ones) else ones
        if len(inputValues) == 1: return inputValues[0]
co2, oxygen = number(inputValues,"co2"),number(inputValues,"oxygen")
print(int(co2,2),int(oxygen,2),"\n",int(co2,2)*int(oxygen,2))
