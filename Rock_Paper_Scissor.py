import random as rn
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

game = [rock, paper, scissors]
computer = rn.randint(0,len(game)-1)

#User part
your_choice = int(input("Enter your choice(1,2 or 3)\n 1.Rock \t 2. paper \t 3. scissors\n "))
if your_choice > 3 or your_choice < 1:
    print("Enter valid Number range from 1-3 and YOU LOSEE!!!\n")
    exit()

if your_choice == 1:
    print("You choose rock\n")
    print(rock)
elif your_choice == 2:
    print("You choose paper\n")
    print(paper)
else:
    print("You choose scissors\n")
    print(scissors)

#Computer Part
if computer == 1:
    print("Computer choose rock\n")
    print(rock)
elif computer == 2:
    print("Computer choose paper\n")
    print(paper)
else:
    print("Computer choose scissors\n")
    print(scissors)

#Game Logic
if your_choice == 1 and computer == 3:
    print("You WIN!!\nROCK beats SCISSORS!!")
elif your_choice == 2 and computer == 1:
    print("You WIN!!\nPAPER beats ROCK!!")
elif your_choice == 3 and computer == 2:
    print("You WIN!!\nSCISSORS beats PAPER!!")
elif your_choice == computer:
    print("It's a DRAW!!!\n")
else:
    print("Computer WINS!!\n You LOSE!!\n")


