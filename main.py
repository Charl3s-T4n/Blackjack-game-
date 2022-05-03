############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

from replit import clear
from art import logo 

def blackjack():          # Create function which will execute the game when called ----> so that i can restart the game when user wants to     ( PROGRAM INDENTED UNDER THIS )
  print(logo)

  import random 
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_randomly_chosen = random.choice(cards)             # Randomly choose a number from the list 
    return card_randomly_chosen

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  user_cards.append(deal_card())     # Randomly draw first card
  user_cards.append(deal_card())     # Randomly draw second card

  computer_cards = []
  computer_cards.append(deal_card()) # Randomly draw first card
  computer_cards.append(deal_card()) # Randomly draw second card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
  def calculate_score(list_of_cards):
    score = sum(list_of_cards)
    if score > 21 and 11 in list_of_cards:       # HINT 8
      list_of_cards.remove(11)
      list_of_cards.append(1)
      score = sum(list_of_cards)
      return score 
    if len(list_of_cards) == 2 and score == 21:    # HINT 7: Scenario where 2 cards and score = 21
      return 0
    else:
      return score 

  user_score = calculate_score(list_of_cards = user_cards)      # Score for user
  computer_score = calculate_score(list_of_cards = computer_cards)     # Score for computer 

  print(f" Your cards: {user_cards}, current score: {user_score}" )
  print(f" Computer's first card: {computer_cards[0]}")


  def draw_card_again():              # Create function that will add another card to the list for user
    user_cards.append(deal_card())      # Draw another card for user --> adds another card to the list
  
  def computer_draw_card_again():     # Create function which adds card to computer's list
    computer_cards.append(deal_card()) 

  while computer_score < 17:    # HINT 12
    computer_draw_card_again() 
    computer_score = calculate_score(list_of_cards = computer_cards)

  def final_winner():      # Create function which will print whose the winner
    if user_score > 21 and computer_score > 21:             # If both exceed 21
      print("It's a draw! You both exceeded 21!")
    elif user_score < 22 and user_score > computer_score:
      print("Congrats, you won! You have more points! ")
    elif user_score == computer_score:
      print("It's a draw! ")
    elif user_score > 21 and user_score > computer_score:
      print("Awww, you lost! You have exceeded 21!")
    elif computer_score > user_score and computer_score > 21:
      print('Congrats, you won! Computer has exceeded 21!')
    elif user_score < computer_score:
      print('Awww, you lost! Computer has more points!')

    restart_game = input("Do you want to restart the game? Type 'yes' to restart or 'no' if otherwise: ").lower()      # This will be asked to the user whenever final_winner() is declared 
    if restart_game == 'yes':
      clear()
      blackjack()         # Call back the program (RESTART) 
    elif restart_game == 'no':
      print("Ok, goodbye!")

  
  if user_score == 0 or computer_score == 0:     # HINT 9: Scenario where computer or user has blackjack
    if user_score > computer_score:
      print(f"Your final hand: {user_cards}, final score: {user_score}")
      print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
      print("Game over! Computer has gotten blackjack 21 points and won!")
      restart_game = input("Do you want to restart the game? Type 'yes' to restart or 'no' if otherwise: ").lower()      # This will be asked to the user whenever a winner is declared (from winning from blackjack 21 points)
      if restart_game == 'yes':
        clear()
        blackjack()         # Call back the program (RESTART) 
      elif restart_game == 'no':
        print("Ok, goodbye!")
    elif user_score < computer_score:
      print(f"Your final hand: {user_cards}, final score: {user_score}")
      print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
      print("Game over! User has gotten blackjack 21 points and won!")
      restart_game = input("Do you want to restart the game? Type 'yes' to restart or 'no' if otherwise: ").lower()      # This will be asked to the user whenever a winner is declared (from winning from blackjack 21 points)
      if restart_game == 'yes':
        clear()
        blackjack()         # Call back the program (RESTART) 
      elif restart_game == 'no':
        print("Ok, goodbye!")
    else:
      print(f"Your final hand: {user_cards}, final score: {user_score}")
      print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
      print("It's a draw! Both user and computer have gotten blackjack 21 points!")
      restart_game = input("Do you want to restart the game? Type 'yes' to restart or 'no' if otherwise: ").lower()      # This will be asked to the user whenever a winner is declared (from winning from blackjack 21 points)
      if restart_game == 'yes':
        clear()
        blackjack()         # Call back the program (RESTART) 
      elif restart_game == 'no':
        print("Ok, goodbye!")
  else:                 # If game not ended, where nobody got blackjack or points > 21
    while user_score < 21:     # while user score always below 21, ask whether to draw another card
      draw_another_card_for_user = input("Type 'y' to draw another card. Type 'n' to pass: ").lower()  # HINT 10
      if draw_another_card_for_user == 'y':   # want to draw while user score still below 21
        draw_card_again()
        user_score = calculate_score(list_of_cards = user_cards)  # New score when draw another card
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")
        if user_score == 21:      # Score AFTER DRAWING ADDITIONAL CARD
          print(f"Your final hand: {user_cards}, final score: {user_score}")
          print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
          final_winner()
        elif user_score > 21:     # SCORE AFTER DRAWING ADDITIONAL CARD
          print(f"Your final hand: {user_cards}, final score: {user_score}")
          print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
          final_winner()
      elif draw_another_card_for_user == 'n':      # elif never draw additional card at all
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        final_winner()
        break       # break out of while loop so program will end 
      if draw_another_card_for_user == 'n':   # don't want to draw while user score stll below 21
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        final_winner()
        break       # break out of while loop so program will end


blackjack()   # This will start the program running the first time 



#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

