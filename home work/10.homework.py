import keyword

user_in = input()
user_in_count = 0
valid = True
punctuation = ['!', "'", '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', ' ', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', "]", '^', '`', '{', '|', '}', '~']

for i in user_in:
    if i in punctuation or i.isupper():
        valid = False
        break
    elif user_in in keyword.kwlist:
        valid = False
        break
    elif user_in[0].isdigit():
        valid = False
        break
    elif i.isdigit():
        continue
    elif i == '_':
        user_in_count += 1
        if user_in_count > 1:
            valid = False
            break
    elif not i.isalpha():
        valid = False
        break
    else:
        user_in_count = 0
print(valid)









