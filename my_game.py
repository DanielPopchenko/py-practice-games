import os
import random

print("Welcome to game: 'Numbers'!")

while True:
    print("""
        Type 'start' to start the game
        Type 'help' to see game info and rules
        Type 'exit' to leave the game 
    """)

    command = input('->')

    if command == 'start':
        break
    elif command == 'help':
        print("""
            Game 'Numbers' will help you to improve your memory!

            Game rules: 
                1) After starting a game, in console will appear one random number
                2) You need to type this number
                3) If you typed right number, the game will continue, and the next number will show
                4) Then, you need to type two numbers, previous and current number
                5) The game will go on up to the first mistake

            """)
    elif command == 'exit':
        exit()
    else:
        print('Incorrect command, try again!')

b = ''

while True:
    os.system('cls||clear')
    a = str(random.randint(0, 9))
    print(f'Current number: {a}')
    command = input('Type your answer: ')

    c = a + b

    if command == c:
        print('The answer is right!')
        b = command
        continue
    else:
        print(f'Error! The right answer - {c}')
        print(f'Your answer - {command}')
        break