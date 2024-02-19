number = int(input('Введіть будь-яке 4-х значне число:'))
x = 10
a, b = divmod(number, x)
c, d = divmod (a, x)
f, e = divmod (c, x)
print (f)
print (e)
print (d)
print (b)