n1 = int(input("Введіть перше число:"))
n2 = int(input("Введіть друге число:"))
r = input("Введіть дію:")
if r == '+':
    print('Результат:',n1+n2)
elif r == '-':
    print('Результат:',n1-n2)
elif r == '*':
    print('Результат:',n1*n2)
elif r == '/':
    if n2 != 0:
        print('Результат:',n1/n2)
    else:print('Результат: на нуль ділити не можна!')