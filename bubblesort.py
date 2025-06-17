list = [ 12, 34, 2, 5, 7]

for i in range(0, len(list)):
    for j in range(i, len(list)):
        if list[i] > list[j]:
            list[i],list[j]= list[j], list[i]

print(list)            