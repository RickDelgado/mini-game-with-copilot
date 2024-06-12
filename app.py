#import the random module
import random

#Create a while loop that will run while the user entered yes in the console to the question, Do You Want To Play Again?
#If the user enters yes, the game will start again. If the user enters no, the game will end.
#If the user enters anything other than yes or no, the game will ask the user to enter yes or no.

#add three variables to keep track of the user's score, the computer's score and the number of ties
user_score = 0
computer_score = 0
ties = 0


while True:
    #ask the user for his/her input Rok Scissors  or Paper and evalaute if the input is valid, if not ask the user to enter a valid input
    print('Enter Rock, Paper or Scissors')
    user_input = input().lower()
    if user_input not in ['rock', 'paper', 'scissors']:
        print('Please enter a valid input')
        continue
    #generate a random to decide the computer's choice between Rock, Paper or Scissors
    #evaluate the result of the game and determine the winner
    #set user_input to lower case
    user_input = user_input.lower()

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f'Computer choice is {computer_choice}')
    if user_input == computer_choice:
        print('It is a tie')
        ties += 1
    elif user_input == 'rock' and computer_choice == 'scissors':
        print('You win')
        user_score += 1
    elif user_input == 'rock' and computer_choice == 'paper':
        print('Computer wins')
        computer_score += 1
    elif user_input == 'paper' and computer_choice == 'rock':
        print('You win')
        user_score += 1
    elif user_input == 'paper' and computer_choice == 'scissors':
        print('Computer wins')
        computer_score += 1
    elif user_input == 'scissors' and computer_choice == 'paper':
        print('You win')
        user_score += 1
    elif user_input == 'scissors' and computer_choice == 'rock':
        print('Computer wins')
        computer_score += 1

    #ask the user if he/she wants to play again

    print('Do You Want To Play Again? (yes or no)')
    answer = input().lower()
    if answer == 'yes':
        print('The game will start again')
        continue
    elif answer == 'no':
        #print the user's score, the computer's score and the number of ties
        print(f'User score is {user_score}')
        print(f'Computer score is {computer_score}')
        print(f'Number of ties is {ties}')
        break
    else:
        print('Please enter yes or no')
        


