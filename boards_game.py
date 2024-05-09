import random
import time

def create_board(rows, cols):
    # ? Created a 2D array with random number between 1 and 9
    board = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
    return board

def print_board(board):
    for row in board:
        print(' '.join(str(num) for num in row))

def play_game():

    print("Welcome to Guess the Number!")
    time.sleep(0.3)
    print("Guess a number between 1 and 9.")

    print()
    print('Remember, the more rows and columns are, the harder the game is.')
    print('...')
    time.sleep(2.5)
    
    rows = int(input('Now, please choose a number of rows: '))
    cols = int(input('Then,  choose a number of columns: '))
    max_attempts = 10

    board = create_board(cols, rows)

    
    print(f"You have {max_attempts} attempts.")
    time.sleep(1)
    print_board(board)

    target_row = random.randint(0, rows - 1)
    target_col = random.randint(0, cols - 1)
    target_number = board[target_row][target_col]
    print('target_number:', target_number)

    attempts = 0
    while attempts < max_attempts:
        guess_row = int(input("Guess the row (0 to {}): ".format(rows - 1)))
        guess_col = int(input("Guess the column (0 to {}): ".format(cols - 1)))

        if guess_row == target_row and guess_col == target_col:
            print(f"Congratulations! You guessed the number {board[guess_row][guess_col]}!")
            return

        print("Wrong guess. Try again.")
        attempts += 1

    print("You've run out of attempts. The target number was {}.".format(target_number))



