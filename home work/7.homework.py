#l = [0, 1, 0, 12, 3]
#l = [0]
#l = [1, 0, 13, 0, 0, 0, 5]
l = [9, 0, 7, 31, 0, 45, 45, 0, 45, 0, 0, 96, 0]
print(l, end=' -> ')
list = []
k = 0
for i in l:
    if i != 0:
        list.append(i)
    else:
        k += 1
list = list + [0] * k
print(list)
