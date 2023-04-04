import os

def check(secret, guess): 
    if guess > secret:
        return 'more', 0
    elif guess < secret:
        return 'less', 0
    else:
        return 'equal', 1


os.system('cls' if os.name == 'nt' else 'clear')

secret = input('Think of a secret number >> ')
os.system('cls' if os.name == 'nt' else 'clear')

attempts_int = int(input('how many attempts do you give him? >> '))
os.system('cls' if os.name == 'nt' else 'clear')

resul2 = 0

while resul2 == 0 and attempts_int > 0:
    guess = input(f'You have {attempts_int} tries to guess the number >> ')
    os.system('cls' if os.name == 'nt' else 'clear')

    resul1, resul2 = check(secret, guess)

    if resul2 == 1:
        print('You guessed the number!! ;)')

    elif attempts_int == 1:
        print(f"You didn't guess the number. The guessed number is {resul1}. You have run out of things to try. :(")

    else:
        print(f"You didn't guess the number. The guessed number is {resul1}.")

    attempts_int -= 1
