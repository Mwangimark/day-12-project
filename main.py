import art
import random

print(art.logo)
print("Welcome to the number Guessing Game !")
print("I'm thinking of a number between 1 and 100 .")
user_input = input("Choose a Level : type 'easy' , or type 'hard' : ") 
comp_random_number = random.randint(1,100)

def operations():
  user_guess = int(input("Make a guess : "))
  if user_guess == comp_random_number:
    print(f"You got it ! The answer was {user_guess}")
    return True
  elif user_guess > comp_random_number:
    print("Too high")
  else: 
    print("Too low")
  return False

if user_input == "easy":
  guess_loop = 11
  for i in range (1,guess_loop):
    print(f"You have {guess_loop-1} attempts remaining to guess the number .")
    guess_loop -= 1  
    if operations():
      break

if user_input == "hard":
  guess_loop = 6
  for i in range (1,guess_loop):
    print(f"You have {guess_loop -1} attempts remaining to guess the number .")
    guess_loop -= 1  
    if operations():
      break

print("Game Over !!")