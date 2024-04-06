import random

def play_game():
    choices = ['Камінь', 'Ножиці', 'Папір']
    user_input = input('Вітаю! Щоб розпочати гру "Камінь, ножиці, папір", введіть ваш вибір: ').capitalize()
    if user_input in choices:
        print('Ваш вибір:', user_input)
    else:
        print('Неправильне введення, спробуйте ще раз')
        return

    ai_choice = random.choice(choices)
    print("Комп'ютер вибрав:", ai_choice)
    if (ai_choice == 'Камінь' and user_input == 'Ножиці') or \
       (ai_choice == 'Папір' and user_input == 'Камінь') or \
       (ai_choice == 'Ножиці' and user_input == 'Папір'):
        print('Ви програли')
    elif ai_choice == user_input:
        print('Нічия')
    else:
        print('Ви виграли')

play_game()