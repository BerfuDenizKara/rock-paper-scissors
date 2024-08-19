import random
import time

# Explains the game rules and options to the user
rps_game_info = """Welcome to Rock Paper Scissors Game 

                    Rules:
                        You can choose one of the following options:
                            - rock
                            - paper
                            - scissors

                        * Rock beats scissors
                        * Scissors beats paper
                        * Paper beats rock
                        It is a tie if you and the computer choose the same option.

                    Game:
                        You will be playing against the computer.
                        You will be playing until one of you wins 2 times in one game.
                        If you want to play again, you can type 'yes'.
                        If you want to exit the game, you can type 'exit'.\n\n"""

print(rps_game_info)

rps_game_options = ['rock', 'paper', 'scissors']
game_continue = ['yes', 'no']

# Function to get the user's choice and the computer's choice
def _choice_():
    # This will be used to determine whether game is on or not
    game = True

    # taking user's choice
    user_choice = input("\nEnter your choice of " + 
                        "'rock', 'paper', 'scissors' or 'exit' : ")
    while True:
        # If user wants to exit the game
        if user_choice == "exit":
            game = False
            break
        # If user's choice is one of the game options
        elif user_choice in rps_game_options:
            break
        # If user enters an invalid choice
        else:
            print("Invalid choice. Please try again.")
            user_choice = input("\nEnter your choice of " + 
                                "'rock', 'paper', 'scissors' or 'exit' : ")

    # User exits the game
    if not game:
        print("\nGame is over.")

    # Computer's choice
    computer_choice = random.choice(rps_game_options)
    print("\nMy choice: " + computer_choice)

    return user_choice, computer_choice, game

# Function to play the game
def tas_kagit_makas_BERFUDENIZ_KARA():      

    # Initialising the total wins of user and computer
    user_total_win = 0
    computer_total_win = 0

    # Taking the user's choice and the computer's choice
    user_choice, computer_choice, game = _choice_()

    # Game loop
    while game:
        # Rounds loop until one of the players win 2 rounds in total
        while (user_total_win < 2 and 
              computer_total_win < 2):
            # Tie
            if user_choice == computer_choice:
                print("\nIt is a tie! What a waste of time... Score: You: " , 
                      user_total_win , " Me: " , computer_total_win)
            # User wins, user = rock, computer = scissors
            elif (user_choice == "rock" and 
                  computer_choice == "scissors"):
                user_total_win += 1
                print("\nYou win :( Score: You: " , user_total_win , 
                      " Me: " , computer_total_win)
            # User wins, user = paper, computer = rock              
            elif (user_choice == 'paper' and 
                  computer_choice == "rock"):
                user_total_win += 1
                print("\nYou win :( Score: You: " , user_total_win , 
                      " Me: " , computer_total_win)
            # User wins, user = scissors, computer = paper
            elif (user_choice == 'scissors' and 
                  computer_choice == "paper"):
                user_total_win += 1
                print("\nYou win :( Score: You: " , user_total_win , 
                      " Me: " , computer_total_win)
            # Computer wins, other options
            else:
                computer_total_win += 1
                print("\nHa Ha!! You loser! Score: You: " , user_total_win , 
                      " Me: " , computer_total_win)
            # If the game is not over, take the user's choice and the computer's choice again
            if (user_total_win < 2 and 
                computer_total_win < 2):
                user_choice, computer_choice, game = _choice_()

        # If the game is over    
        print("\nGame is finished.")
        print("Final Score: You: " , user_total_win , 
              " Me: " , computer_total_win)

        # Total win count is reset for the new game
        user_total_win = 0
        computer_total_win = 0

        # Asking user and computer if they want to play again or not
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ")
            # If user wants to play again
            if play_again == "yes":
                print("Great! Let me think...")
                time.sleep(3)
                # If computer wants to play again
                if random.choice(game_continue) == "yes":
                    print("Okay, let's play again! I feel lucky :)")
                    break
                # If computer doesn't want to play again
                else:
                    print("Naah, maybe another time!")
                    game = False
                break
            # If user doesn't want to play again
            elif play_again == "no":
                print("Thanks for playing. See you!")
                game = False
                break
            # If user enters an invalid choice
            else:
                print("Invalid choice. Please try again.")

tas_kagit_makas_BERFUDENIZ_KARA()