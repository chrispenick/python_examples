'''The is the guessing game module.
You can guess a number and get insulted by the program.'''
from random import randint

# let the user cheat with a command line option
# check for cheat code

# get the random number and setup game
def main():
    secret = randint(1,100)
    guess = -1
    print(f"Psst! The secret number is {secret}. Shhh!")

    while guess != secret:
        # get some input from the user
        guess = int(input('Guess the secret number: '))
        print(f"You entered the number: {guess, type(guess)}")
        
        # check and win or go back
        if guess == secret:
            print("Yay you guessed the secret number.")
        else:
            quit = input("Do you want to give up? ").lower()
            if quit == 'y' or quit == 'yes':
                print("See ya quitter")
                break

if __name__ == '__main__':
    main()
