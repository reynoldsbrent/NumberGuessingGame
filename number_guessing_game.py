import random
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import numpy as np
number_range = int(input("Please enter a number range: "))
random_number = random.randint(1, number_range)
guess = False
quit = ''
guess_list = []
games_played = 0
games_played_list = []
while quit != 'Q':
    games_played += 1
    games_played_list.append(games_played)
    number = int(input("Please enter a guess: "))
    guesses = 1
    guess = False
    random_number = random.randint(1, number_range)
    while guess == False:
        if number == random_number:
            guess = True
            print("Congrats! You guessed the right number!")
        else:
            if number < random_number:
                print("Your guess was too low.")
            else:
                print("your guess was too high.")
            number = int(input("You guessed incorrecty. Please enter a guess: "))
            guesses += 1
    guess_list.append(guesses)
    if guesses == 1:
        print(f"It took you {guesses} guess.")
    else:
        print(f"It took you {guesses} guesses.")
    quit = input("To quit the game enter Q otherwise press enter to play another game: ")
np_guess_list = np.array(guess_list)
np_num_of_games = np.array(games_played_list)
plt.figure(dpi = 100)
plt.bar(np_num_of_games, np_guess_list)
plt.title('Guessing Game Results')
plt.xlabel('Game Number')
plt.ylabel('Number of Guesses')
plt.show()
# TODO Remove decimal points from y-axis 