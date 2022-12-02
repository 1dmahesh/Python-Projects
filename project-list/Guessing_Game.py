import random
from termcolor import colored, cprint

color = colored("Yehh!! , It's Game time ", "red", attrs=['reverse', 'bold'] )
print(color)
print()


def select_game():
    print("A.", '\033[1m' + 'User_Guess' + '\033[0m')
    print("B.", '\033[1m' + 'Computer_guess' + '\033[0m')
    Game = input("Which Game do you want to Play: ")
    if Game == "a" or Game == "A": 
        print('You have chosen', '\033[1m' + 'User_Guess' + '\033[0m')
        print()
        guess(50)
    else :
        Game == "b" or Game == "B",
        print(f'You have choosen', '\033[1m' + 'Computer_guess' + '\033[0m')
        print()
        computer_guess(50)



def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, Your Guess is too low.')
        elif guess > random_number:
            print('Sorry, Your Guess is too high.')
    print()
    color_computer = colored("Yeah, You have guessed it Right, The number is " + str(int(guess)), "green", attrs=['reverse', 'bold', 'blink'])
    print(color_computer)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess_com = random.randint(low, high)
        feedback = input(f'Is {guess_com} too high (H), too low (L), or if you hit jackpot press (c)?? '.lower())
        if feedback == 'h':
            high = guess_com - 1
        elif feedback == 'l':
            low = guess_com + 1
    print()
    success_color = colored('Yeah, Computer has guessed your Number correctly, which is ' + str(int(guess_com)) , "green", attrs=['reverse', 'bold','blink'])
    print(success_color)

select_game()
