import random
import time

def launch_the_game():
    start = input('Вы запустили игру "Камень, ножницы, бумага". Хотите поиграть? (Вводите + или -): ')

    if start == '+':
        print('Загрузка...')
        time.sleep(1)
        print("Загрузка завершена! Начинаем!")
        time.sleep(0.7)
        print("3...2...1...")
        time.sleep(0.6)
        print('Если захотите закончить вводите "-".')
        print('Если захотите узнать счёт вводите "с". Вы сможете узнать счет только после 1 сессии игры!')
        user_ball = 0
        rand_ball = 0
        while True:
            user = input("Камень, ножницы или бумага? (Вводите к, н или б): ")
            list_play = ['к', 'н', 'б']
            if user == 'с':
                print('Сыграйте как минимум 1 партию!')

        # Если ответ юзера совпадает с елементом списка, делаем проверки
            if user in list_play:
                rand = random.choice(list_play)
                print(f"Выбор соперника - {rand}")
                print(f"Ваш выбор - {user}")


            if rand == 'к' and user == 'н':
                print('+ 1 балл сопернику')
                rand_ball += 1
            if rand == 'к' and user == 'б':
                print('+ 1 балл вам')
                user_ball += 1
            if rand == 'н' and user == 'к':
                print('+ 1 балл вам')
                user_ball += 1
            if rand == 'н' and user == 'б':
                print('+ 1 балл сопернику')
                rand_ball += 1
            if rand == 'б' and user == 'н':
                print('+ 1 балл вам')
                user_ball += 1
            if rand == 'б' and user == 'к':
                print('+ 1 балл сопернику')
                rand_ball += 1
            if rand == 'б' and user == 'б':
                print('Ничья')
            if rand == 'к' and user == 'к':
                print('Ничья')
            if rand == 'н' and user == 'н':
                print('Ничья')
            
            elif user_ball == 0 and rand_ball == 0 and user == '-':
                print('Вы еще не начали игру, нету счета!')
            elif user == 'с':
                print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")
            elif user == '-':
                print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")
                print('Конец игры! Заходите ещё!')
                break
            
    else:
        print('Вводите к, н или б')


    if start == '-':
        print(' А жаль... :(')