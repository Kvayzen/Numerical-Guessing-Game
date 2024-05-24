import random
def play_game():
    num = random.randint(1, 100)
    print('Добро пожаловать в числовую угадайку!\n')

    for count in range(10):
        print(f'У вас осталось {10 - count} попыток')
        while True:
            try:
                number = input('Введите число от 1 до 100 или напишите "закончить игру": \n')
                if number.lower() == 'закончить игру':
                    return
                number = int(number)
                if 1 <= number <= 100:
                    break
                else:
                    print("А может быть все-таки введем целое число от 1 до 100?\n")
            except ValueError:
                print("А может быть все-таки введем целое число от 1 до 100?\n")

        if number < num:
            print(f'Ваше число: {number} МЕНЬШЕ загаданного, попробуйте еще разок\n')
        elif number > num:
            print(f'Ваше число: {number} БОЛЬШЕ загаданного, попробуйте еще разок\n')
        else:
            print('ПОЗДРАВЛЯЕМ! Вы угадали!\n' + 'Вам потребовалось: ', count+1, 'попыток\n' +'Если хотите сыграть еще раз напишите: "Хочу еще"\n')
            while True:
                play_again = input('Введите "хочу еще" или "выход"').lower()
                if play_again == 'хочу еще':
                    play_game()
                    break
                elif play_again == 'выход':
                    return
                else:
                    print('Неверный ввод, попробуйте снова\n')
    if count == 9:
        print("К сожалению, попытки закончились. Попробуйте еще раз!\n")
        play_game()
        return

while True:
    print('Введите название игры "угадайка" или "выход", чтобы закончить:')
    user_input = input().lower()
    if user_input == 'угадайка':
        play_game()
    elif user_input == 'выход':
        break
    else:
        print('Неверное название игры, попробуйте снова\n')