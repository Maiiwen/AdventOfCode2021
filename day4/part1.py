from splitInputToList import openFileToTab
score = 0
grids, tab = openFileToTab()
for i in range(len(grids)):
    grid = grids[i]
    for j in range(5):
        gridContent = grid[j]
        gridContent = gridContent.split()
        grid[j] = gridContent
    grids[i] = grid
def updateGrid(grid,num):
    for j in range(len(grid)):
        if num in grid[j]:
            gridContent = grid[j]
            for k in range(len(gridContent)):
                if num == gridContent[k]:
                    gridContent[k] = '100'
                    grid[j] = gridContent
    return grid
def check(grids):
    for i in range(len(grids)):
        for j in range(len(grids[i])):
            try :
                if (grids[i][j] == '100' and grids[i+1][j] == '100' and grids[i+2] [j] == '100' and grids[i+3][j] == '100' and grids[i+4][j] == '100') or (grids[i][j] == '100' and grids[i][j+1] == '100' and grids[i][j+2] == '100' and grids[i][j+3] == '100' and grids[i][j+4] == '100'):
                    return 'end'
            except:
                continue
for j in range(len(tab)):
    for i in range(len(grids)):
        grids[i] = updateGrid(grids[i],str(tab[j]))
        test = check(grids[i])
        if test == 'end':
            print(i+1,tab[j])
            winingGrid = grids[i]
            num = tab[j]
            break
    if test == 'end':
        break
    winingGrid = i
for i in range(len(winingGrid)):
    for j in range(len(winingGrid[i])):
        if winingGrid[i][j] != '100': score += int(winingGrid[i][j])
print(score*num)
