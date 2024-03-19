print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;  X  (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "   X  `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is... to find the treasure!") 

action1 = input("\nTwo paths, but you've gotta make a choice. Where do you go? [Left / Right]: ").lower()

if action1 == "right":
  print("You plunge into the abyss. GAME END. [Bad Ending 1: Disappointing Death]")
elif action1 == "left":
  action2 = input("\nYou come across a quaint lake, with a strange chest in the middle. What do you do? [Swim / Wait]: ").lower()
  if action2 == "swim":
    print("\nWading into the lake for a swim... you quickly discover that the shrine is a mimic, and it devours you before you can react. GAME END. [Bad Ending 2: Surprise Mechanics]")
  elif action2 == "wait":
    action3 = input("\nWith some patience... the world around you fades away. You find yourself before three coloured doors in a dungeon. Could the treasure be behind one of these doors? Time to find out. [Red / Blue / Yellow]: ").lower()
    if action3 == "red":
      print("\nYou stumble into the House of Hope fight with Raphael. Barrelmancer-specced Tav throws a fireball and the thermonuclear force of the sun vaporizes you. GAME END. [Bad Ending 3: Baldur's Loss]")
    elif action3 == "blue":
      print("\nBehind the sapphire blue door you find Toby the dog! He is very large, but means well. He barks and your weak heart can't take it, so you die. GAME END. [Bad Ending 4: Toby Cameo]")
    elif action3 == "yellow":
     print("\nCheems the friendly yellow dog descends from the heavens and greets you. He shows you the way to the treasure, and you gently hold his paw in your hand as you let go and subsequently watch him re-ascend to the heavens. GAME END. [Good Ending: Cheems' Treasure Island")
    else:
      print("\nSomething strange is happening... the dungeon doesn't take kindly to you attempting to exit it's bounds. It implodes with you inside it. GAME END. [Bad Ending 5: Tricked...]")