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

player = [rock, paper, scissors]
computer = [rock, paper, scissors]

choice_player = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
choice_computer = random.randint(0,2)

if choice_player >= 3 or choice_player < 0:
  print("You choice an invalid number")
else:
  player_picture = player[choice_player]
  computer_picture = computer[choice_computer]
  
  print(player_picture)
  print(computer_picture)
  
  if choice_player == choice_computer:
    print("It's a Tie!")
  elif choice_player == 0 and choice_computer == 1:
    print("The Computer won!")
  elif choice_player == 0 and choice_computer == 2:
    print("You Won!")
  elif choice_player == 1 and choice_computer == 2:
    print("The Computer won!")
  elif choice_player == 1 and choice_computer == 0:
    print("You Won!")
  elif choice_player == 2 and choice_computer == 0:
    print("The Computer won!")
  elif choice_player == 2 and choice_computer == 1:
    print("You Won!")