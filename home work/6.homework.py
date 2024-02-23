#list = [12, 3, 4, 10]
#list = [1]
list = []
#list = [12, 3, 4, 8]
if len(list) > 1:
    a = list.pop()
    list.insert(0, a)
    print(list)
else: print(list)