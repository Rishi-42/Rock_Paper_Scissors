import random

chooices = ['Rock', 'Paper', 'Scissior']
system_guess = random.choice(chooices)

def is_valid(user_guess):
    sample = user_guess
    if (sample.title() == 'Rock') or  (sample.title() == 'Paper') or (sample.title() == 'Scissior'):
        winner(sample)
        print(f'The system guessed {system_guess} where as you guessed {user_guess}')
            
    else:
        print('Please provide valid input.')

def winner(sample):
    if sample == system_guess:
        print(f"It's a tie!")
    elif sample == "rock":
        if system_guess == "scissors":
            print("You smashed the scissors! You win!")
        else:
            print("You got covered by the Paper covers rock! You lose.")
    elif sample == "paper":
        if system_guess == "rock":
            print("You covered the rock! You win!")
        else:
            print("The Scissors cuts you ! You lose.")
    elif sample == "scissors":
        if system_guess == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("You are smashed by Rock! You lose.")

user_input = str(input("Enter your guess : "))
is_valid(user_input)