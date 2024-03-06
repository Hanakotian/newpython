user = input('ВВедіть число:')

while True:
    a = 1
    for i in user:
        a *= int(i)
    if a <= 9:
        break
    user = str(a)
print('Добуток = ', a)