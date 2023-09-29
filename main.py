from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  #Formating of account data as name, description and country
  name_account = account["name"]
  desc_account = account["description"]
  country_account = account["country"]
  return f"{name_account}, a {desc_account}, from {country_account}."

#Checking if user's guess is correct
def check_answer(guess, first_followers, second_followers):
  if first_followers > second_followers:
    return guess == "a"
  else:
    return guess == "b"

print(logo)
score = 0
continue_game = True
second_account = random.choice(data)

while continue_game:
  #Ensuring account B is shifted to A for next question
  first_account = second_account
  second_account = random.choice(data)
 
  while first_account == second_account:
    second_account = random.choice(data)
  
  print(f"Compare A: {format_data(first_account)}.")
  print(vs)
  print(f"Against B: {format_data(second_account)}.")
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  first_follower_count = first_account["follower_count"]
  second_follower_count = second_account["follower_count"]
  win_round = check_answer(guess, first_follower_count, second_follower_count)

  #Clearing the screen in between rounds  
  clear()
  print(logo)
  
  #Giving user feedback on their guess and point system
  if win_round:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    continue_game = False
    print(f"Sorry, wrong answer. Final score: {score}.") 