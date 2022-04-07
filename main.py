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

input =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

random_num=int(random.randint(0,2))
if input==0:
  print(rock)
elif input==1:
  print(paper)
else:
  print(scissors)

if random_num==0:
  computer=rock
if random_num==1:
  computer=paper
if random_num==2:
  computer=scissors

print(f"Computer chose:\n{computer}\n")

if random_num==input:
  print("Draw")
elif random_num==0 and (input==1):
  print("You Win")
elif random_num==0 and (input==2):
  print("You Loose")
elif random_num==1 and (input==0):
  print("You Loose")
elif random_num==1 and (input==2):
  print("You Win")
elif random_num==2 and (input==0):
  print("You Win")
elif random_num==2 and (input==1):
  print("You Loose")