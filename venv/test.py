def list_from_first_el(index, lst, dir):
    newList = []
    if dir == 'front':
        for i in range(index, len(lst)):
            newList.append(lst[i][0])
    else:
        for i in range(index+1):
            newList.append(lst[i][0])
    return newList


lst = ['PRP', 'VBP', 'NN', 'CC', 'PRP', 'VBP', 'RB', 'VB', 'NN', 'NN', 'NN']
i=2
print(lst[0][-1])