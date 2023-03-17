# "_Numbers_" Game

---

## This game will impove your memory and you`ll definately have fun!

---

![image](https://www.sciencenews.org/wp-content/uploads/2018/05/050718_EC_numbers_feat.jpg)

## The rules are not complicated :

##### 1) After starting a game, in console will appear one random number

##### 2) You need to type this number

##### 3) If you typed right number, the game will continue, and the next number will show

##### 4) Then, you need to type two numbers, previous and current number

##### 5) The game will go on up to the first mistake

---

## Programm code, simple as rules:

```python
# Initialize os, random modules
import os
import random

print("Welcome to game: 'Numbers'!")


# endless loop, we want to wait until user`s answer is 'start'
while True:
    print("""
        Type 'start' to start the game
        Type 'help' to see game info and rules
        Type 'exit' to leave the game
    """)

    # user input variabe
    command = input('->')

    # We will break our loop only when variabe 'command' uquals 'start'
    if command == 'start':
        break
    # By entering this command we can see game rules
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
        # Exits programm
        exit()
    else:
        print('Incorrect command, try again!')

# b - is empty srting just to put entered nums here
b = ''

while True:
    # If user`s answer was 'start', console clears and we begin to play a game
    os.system('clear')

    # variable 'a' is for storing random num
    a = str(random.randint(0, 9))
    print(f'Current number: {a}')

    # User`s answer
    command = input('Type your answer: ')

    # We`re saying that c is random num + (by this moment) emty variable
    # Actually it keeps our num that we should remember
    c = a + b

    # If user`s input equals to c variable ...
    if command == c:
        print('The answer is right!')

        # Empty variable we wrote just above is now not empty
        # Now it`s storing user`s answer
        b = command
        continue
    else:
        print(f'Error! The right answer - {c}')
        print(f'Your answer - {command}')
        # Breaking loop if command is not required number
        break
```

![thanks](http://edvista.com/claire/tutorial/pp/img045.jpg)

## That`s actually it, also thanks for playing my game, enjoy 😀
