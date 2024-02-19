number = int(input('Введіть будь-яке ціле, позитивне 5-х значне число:'))
x = 10
a, b = divmod(number, x)
c, d = divmod (a, x)
f, e = divmod (c, x)
g, h = divmod (f, x)
print (b,d,e,h,g)



