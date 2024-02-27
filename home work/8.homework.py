#l = [1, 3, 5]
#l = [6]
l = []
print(l, end =' => ')
list = [l[::2]]
for i in list:
    if i == []:
      print([])
      break
    if i == list.pop():
       found1 = sum(i)
       found = found1 * l.pop()
       print(found)