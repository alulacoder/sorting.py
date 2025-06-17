# Time Complexity - O(n^2)
list = [ 12, 34, 2, 5, 7]

for i in range(0, len(list)):
    minElement = 1000000
    minLocation = -1
    for j in range(i, len(list)):
        if minElement > list[j]:
            minElement = list[j]
            minLocation = j
            list[i], list[j] = list[j], list[i]

list.sort(reverse = True)
print(list)