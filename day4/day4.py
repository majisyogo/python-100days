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

game_images = [rock, paper, scissors]

# user input number
user_choose = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))

# Show the image only when the input is correct.
if 0 <= user_choose <= 2:
    print("You chose:")
    print(game_images[user_choose])
else:
    print("You input an invalid number.")
    exit()

# computer choose number
computer_choose = random.randint(0, 2)
print(f"Computer chose {computer_choose}:")
print(game_images[computer_choose])

# win lose
if user_choose == computer_choose:
    print("Draw!")

elif (user_choose == 0 and computer_choose == 2) or \
     (user_choose == 1 and computer_choose == 0) or \
     (user_choose == 2 and computer_choose == 1):
    print("You win!")

else:
    print("You lose!")
