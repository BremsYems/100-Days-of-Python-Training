import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#          [0]    [1]     [2]
choices = [rock, paper, scissors]

print("It's Rock, Paper, Scissors! Here we go..")


user_move = int(input("\nOptions: 0 => Rock | 1 => Paper | 2 => Scissors\nPick your action: "))

if user_move <=-1 or user_move >= 3:
  print("\nYou BUFFOON. It's rock, paper, scissors... and you've went out of your way to pick a bad option. Failure! YOU LOSE.")
else:
  print(choices[user_move])
  
  ai_move = random.randint(0, 2)
  
  print(f"Enemy AI Action:\n{choices[ai_move]}")

  if user_move == ai_move:
    print("\nIt's a standstill... neither force gives in!")
  elif user_move == 0 and ai_move == 1:
    print("\nYour great stone is no match for your opponent's blanket of white. YOU LOSE.")
  elif user_move == 0 and ai_move == 2:
    print("\nYour great stone pummels the enemy's pathetic scissors. YOU WIN.")
  elif user_move == 1 and ai_move == 0:
    print("\nKertas kau bungkus batu jahat tu. Baiklah. YOU WIN.")
  elif user_move == 1 and ai_move == 2:
    print("\nYour flimsy paper is bisected by the enemy's scissors. YOU LOSE.")
  elif user_move == 2 and ai_move == 1:
    print("\nYour scissors cuts their paper. YOU WIN.")
  elif user_move == 2 and ai_move == 0:
    print("\nYour scissors does 25 dps and the enemy stone has like 5,000 max hp and 40 regen. YOU LOSE.")
  
