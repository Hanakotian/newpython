import random
my_list = []

for i in range(random.randint(3, 10)):
    my_list.append(random.randint(1, 9))
print(my_list, end =' == ' )

k = my_list[0]
n = my_list[2]
e = my_list [-2]
knee = [k, n, e]
print(knee)