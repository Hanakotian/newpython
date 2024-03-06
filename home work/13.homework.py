import string

user = input('Введіть дві літери через дефіс:')
l = user[0]
l2 = user[2]
l = string.ascii_letters.index(l)
l2 = string.ascii_letters.index(l2)
end = string.ascii_letters[l:l2+1]

print("Результат:", end)