import random
import math
from logging import exception
import keyboard
# Global balance and username
balance = 100.0
import time
import turtle
username = ""


# Key state flags
key_state = {
    'w': False,
    's': False,
    'a': False,
    'd': False
}

def run_turtle_game():
    wn = turtle.Screen()
    wn.title("JustAHub, Python Turtle demo.")
    wn.setup(width=600, height=600)
    wn.tracer(0)  # turns off auto updating; smoother movement

    t = turtle.Turtle()
    t.speed(0)

    # move check loop
    def move():
        if key_state['w']:
            t.forward(5)
        if key_state['s']:
            t.backward(5)
        if key_state['a']:
            t.left(5)
        if key_state['d']:
            t.right(5)

        wn.update()
        wn.ontimer(move, 17)  # checks every 17 milliseconds (60 ish FPS)

    # key presses
    def press_w(): key_state['w'] = True
    def release_w(): key_state['w'] = False

    def press_s(): key_state['s'] = True
    def release_s(): key_state['s'] = False

    def press_a(): key_state['a'] = True
    def release_a(): key_state['a'] = False

    def press_d(): key_state['d'] = True
    def release_d(): key_state['d'] = False

    def quit_game():
        wn.bye()

    # Bind keys for press
    wn.onkeypress(press_w, 'w')
    wn.onkeypress(press_s, 's')
    wn.onkeypress(press_a, 'a')
    wn.onkeypress(press_d, 'd')
    wn.onkeypress(quit_game, 'e')

    # Bind keys for release
    wn.onkeyrelease(release_w, 'w')
    wn.onkeyrelease(release_s, 's')
    wn.onkeyrelease(release_a, 'a')
    wn.onkeyrelease(release_d, 'd')

    wn.listen()
    move()  # start the move loops
    wn.mainloop()
def get_wager():
    global balance
    while True:
        try:
            wager = int(input(f"Your current balance is {balance}. Enter your wager: "))
            if wager > balance:
                print("You cannot wager more than your current balance.")
            elif wager <= 0:
                print("Please enter a positive wager.")
            else:
                return wager
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_username():
    global username
    while True:
        response = input("Would you like to use a username? (y/n): ").strip().lower()
        if response == 'y':
            while True:
                username = input("Please enter the username you'd like to use: ").strip()
                if username:
                    return username
                else:
                    print("Username cannot be empty. Please try again.")
        elif response == 'n':
            username = "Guest" + str(random.randint(1, 999))
            return username
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def get_user_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices or choice == 'exit':
            return choice
        print(f"Invalid input. Please enter one of: {', '.join(valid_choices)}")

def get_numbers(use_random):
    if use_random:
        try:
            range1 = int(input('Enter the first number of the range: '))
            range2 = int(input('Enter the second number of the range: '))
            num1 = random.randint(range1, range2)
            num2 = random.randint(range1, range2)
            print(f"Random numbers generated: {num1}, {num2}")
        except ValueError:
            print("Invalid range input. Please enter integers.")
            return None, None
    else:
        try:
            num1_input = input("Enter the first number (or type 'exit' to quit): ")
            if num1_input.lower() == 'exit':
                return None, None
            num1 = float(num1_input)

            num2_input = input("Enter the second number (or type 'exit' to quit): ")
            if num2_input.lower() == 'exit':
                return None, None
            num2 = float(num2_input)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return None, None
    return num1, num2


def factorials():
    while True:
        try:
            print("\nWelcome to the factorial calculator (Inspired by Niko!)")
            print('[1] Factorials')
            print('[2] Superfactorial')
            print('[3] hyperfactorial')
            print('[4] Double/Triple/etc Factorial (Not implemented)')
            print('[5] Subfactorial (Not implemented)')
            print('[6] Primorial (Not implemented)')
            print('[7] Exponential Factorial (Not implemented)')
            print('[0] Back')
            choice = get_user_choice("Choose an operation (0-7): ", [str(i) for i in range(8)])

            if choice == '0':
                break
            elif choice == '1':
                num = int(input("Enter a non-negative integer: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print(f"{num}! = {math.factorial(num)}")
            elif choice == '2':
                num = int(input("Enter the factorial number: "))
                if num <= 0:
                    print("Please enter a positive number.")
                else:
                    result = 1
                    for i in range(1, num + 1):
                        result *= math.factorial(i)
                    print(f"Superfactorial of {num} = {result}")
            elif choice == '3':
                result = 1
                for i in range(1, num + 1):
                    result *= i ** i
                print("Hyperfactorial of {num} = {result}")
            else:
                print("This option is not yet implemented.")
        except ValueError:
            print("Invalid input! Please enter an integer.")
        except Exception as e:
            print("Error:", e)


def advanced_calculator():
    while True:
        print("\nAdvanced Operations (No randoms will be used.):")
        print("[1] Square root")
        print("[2] Power (x^y)")
        print("[3] Sine")
        print("[4] Cosine")
        print("[5] Tangent")
        print("[6] Log base 10")
        print("[7] Natural Log (ln)")
        print("[8] Exponential (e^x)")
        print("[9] Factorial")
        print("[0] Back to main calculator")
        choice = get_user_choice("Choose an operation (0-9): ", [str(i) for i in range(10)])

        try:
            if choice == '0':
                break
            elif choice == '1':
                num = float(input("Enter a number: "))
                print(f"√{num} = ±{math.sqrt(num)}")
            elif choice == '2':
                base = float(input("Enter the base: "))
                exponent = float(input("Enter the exponent: "))
                print(f"{base}^{exponent} = {math.pow(base, exponent)}")
            elif choice == '3':
                angle = float(input("Enter angle in degrees: "))
                print(f"sin({angle}) = {math.sin(math.radians(angle))}")
            elif choice == '4':
                angle = float(input("Enter angle in degrees: "))
                print(f"cos({angle}) = {math.cos(math.radians(angle))}")
            elif choice == '5':
                angle = float(input("Enter angle in degrees: "))
                print(f"tan({angle}) = {math.tan(math.radians(angle))}")
            elif choice == '6':
                num = float(input("Enter a number: "))
                print(f"log10({num}) = {math.log10(num)}")
            elif choice == '7':
                num = float(input("Enter a number: "))
                print(f"ln({num}) = {math.log(num)}")
            elif choice == '8':
                num = float(input("Enter the exponent (x) for e^x: "))
                print(f"e^{num} = {math.exp(num)}")
            elif choice == '9':
                factorials()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print("Error:", e)

def calculator():
    print("\nWelcome to the Python Calculator!")
    use_random = get_user_choice('Use randomly generated numbers? (y/n or "exit" to quit): ', ['y', 'n', 'exit'])

    if use_random == 'exit':
        print("\nBye!")
        return

    use_random = True if use_random == 'y' else False

    while True:
        oper = get_user_choice(
            "Enter an operation (+, -, *, /, ^ for power, or type 'adv' for an advanced calculator, or 'exit' to return to hub): ",
            ['+', '-', '*', '/', '^', 'adv', 'exit']
        )
        if oper == 'exit':
            print("\nBye!")
            break
        elif oper == 'adv':
            advanced_calculator()
            continue

        num1, num2 = get_numbers(use_random)
        if num1 is None or num2 is None:
            return

        try:
            if oper == '^':
                result = math.pow(num1, num2)
            else:
                result = eval(f"{num1} {oper} {num2}")
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception as e:
            print("Calculation error:", e)

def rock_paper_scissors():
    global balance
    print("\nWelcome to Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        if balance <= 0:
            print("Your balance is insufficient.")
            break
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user_choice == 'exit':
            break
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        player_wager = get_wager()
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print(f"{username} wins this round!")
            balance += player_wager
            user_score += 1
        else:
            print("Computer wins this round!")
            balance -= player_wager
            computer_score += 1

        rounds_played += 1
        print(f"Your new balance: {balance}")
        print(f"Score: You {user_score} - Computer {computer_score}")

def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def play_game():
    global balance
    print("\nWelcome to Tic-Tac-Toe!")
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9, or 10 to exit): "))
            if move == 10:
                break
            if move < 1 or move > 9:
                print("Invalid move. Choose a number from 1 to 9.")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] != ' ':
                print("Cell already taken. Choose a different move.")
                continue
            board[row][col] = current_player
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

    print(f"Your new balance is: {balance}")
def number_guessing_game():
    global balance
    print(f"\nWelcome to the Number Guessing Game, {username}!")
    print("Guess a number between 1 and 10.")
    correct_number = random.randint(1, 10)

    while balance >= 10:
        try:
            guess = int(input("Enter your guess (1-10),  win 5x wager if correct, lose 2x if wrong('exit' to leave)): "))
            if guess < 1 or guess > 10:
                print("Invalid guess. Enter a number between 1 and 10.")
                continue
            wager = get_wager()
            if guess == correct_number:
                reward = wager * 5
                balance += reward
                print(f"Correct! You earned {reward} credits. New balance: {balance}")
            else:
                penalty = wager * 2
                balance -= penalty
                print(f"Wrong! The correct number was {correct_number}. You lost {penalty} credits. New balance: {balance}")
            correct_number = random.randint(1, 10)
        except ValueError:
            print("Invalid input. Please enter a number.")
        if balance < 10:
            print("Insufficient balance to continue.")
            break

HANGMAN_STAGES = [
    '''
     -----
     |   |
         |
         |
         |
         |
    ------
    ''',
    '''
     -----
     |   |
     O   |
         |
         |
         |
    ------
    ''',
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    ------
    ''',
    '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    ------
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    ------
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    ------
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ------
    '''
]

def hangman():
    global balance
    word_list = [
        'python', 'hangman', 'programming', 'developer', 'algorithm',
        'flawed', 'jungle', 'rocket', 'powder', 'retain', 'theory',
        'medium', 'killer', 'number', 'defend', 'behave', 'corpse',
        'strong', 'foster', 'remark', 'pierce', 'belief', 'ballet',
        'advice', 'connection', 'abandon', 'dominant', 'instruction',
        'potential', 'paradox', 'foundation', 'settlement', 'limited',
        'dialogue', 'benefit', 'strategic', 'lineage', 'hemisphere',
        'analyst', 'spokesperson', 'holiday', 'elephant', 'performer',
        'announcement', 'consensus', 'dramatic', 'allowance', 'speculate',
        'elegant', 'handicap', 'visual', 'embryo', 'apathy', 'national',
        'gravity', 'grandmother', 'racism', 'romantic', 'privacy',
        'champion', 'different', 'accountant', 'advocate', 'destruction',
        'rhetoric', 'trivial', 'negligence', 'poetry', 'unlikely',
        'employee', 'minister', 'rehearsal', 'compartment', 'censorship'
    ]
    secret_word = random.choice(word_list)
    guessed_word = ['_'] * len(secret_word)
    guessed_letters = set()
    attempts_left = 6
    wager = get_wager()

    print("\nWelcome to Hangman! Try to guess the word.")

    while attempts_left > 0:
        print(HANGMAN_STAGES[6 - attempts_left])
        print(f"Current word: {' '.join(guessed_word)}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Guess a letter (or type 'exit' to quit): ").lower()
        if guess == 'exit':
            print(f"Thank you for playing! The word was: {secret_word}")
            break
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
            if '_' not in guessed_word:
                print(f"\nCongratulations! You guessed the word: {secret_word}")
                balance += wager
                break
        else:
            print("Incorrect guess.")
            attempts_left -= 1
            if attempts_left == 0:
                print(HANGMAN_STAGES[-1])
                print(f"\nGame over! The word was: {secret_word}")
                balance -= wager
                break

def work():
    global balance
    while True:
        no1 = random.randint(1, 20)
        no2 = random.randint(1, 20)
        answer = no1 * no2
        user_input = input(f"\nType 'exit' to leave or solve: {no1} * {no2} = ")
        if user_input == 'exit':
            print("Thanks for working today!")
            break
        elif user_input == str(answer):
            balance += 25
            print(f"Correct! You earned 25 credits. Balance: {balance}")
        else:
            print(f"Incorrect. The correct answer was {answer}.")

def mainhub():
    global balance
    global username

    print(f"\nWelcome to the main hub, {username}. Your balance: {balance}")

    choice = get_user_choice(
        "Choose an option:\n"
        " [1] Calculator\n"
        " [2] Rock, Paper, Scissors\n"
        " [3] Tic-Tac-Toe\n"
        " [4] Number Guessing Game\n"
        " [5] Hangman\n"
        " [6] Work for 25 credits\n"
        " [7] Turtle Movement\n"
        " [credits] See the incredible person who made this!\n> ",
        ['1', '2', '3', '4', '5', '6', '7', 'credits']
    )

    if choice == '1':
        calculator()
    elif choice == '2':
        rock_paper_scissors()
    elif choice == '3':
        play_game()
    elif choice == '4':
        number_guessing_game()
    elif choice == '5':
        hangman()
    elif choice == '6':
        work()
    elif choice == '7':
        run_turtle_game()
    elif choice == 'credits':
        print("Made by Alt2662. Thanks to ChatGPT for optimization, and 'Niko' for inspiration.")




username = get_username()

while True:
    mainhub()
    again = get_user_choice("Would you like to return to the main hub? (y/n): ", ['y', 'n'])
    if again == 'n':
        print("Thanks for playing! Goodbye.")
        break
