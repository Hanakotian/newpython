user = input("Введіть число:")

valid = True
if not user.isdigit() or int(user) < 0 or int(user) > 8640000:
    valid = False

if not valid:
    print("Некоректне введення. Будь ласка, введіть число від 0 до 8640000.")
else:
    day = int(user) // 86400
    ostacha = int(user) % 86400
    hours = ostacha // 3600
    ostacha2 = ostacha % 3600
    minute = ostacha2 // 60
    second = ostacha2 % 60
    day = str(day)
    hours = str(hours)
    minute = str(minute)
    second = str(second)
    if day[-1] == '1':
        print("Результат:", f"{day} день, {hours.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}")
    elif day[-1] == '2' or day[-1] == '3' or day[-1] == '4':
        print("Результат:", f"{day} дні, {hours.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}")
    else:
        print("Результат:", f"{day} днів, {hours.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}")