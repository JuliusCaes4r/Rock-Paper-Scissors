import random

rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

chosen = int(input("What do you choose? type 0 for Rock, 1 for Paper, 2 for Scissors."))

comp = random.randint(0,2)



def choose(rock,paper,scissors,chosen):       
    if chosen == 0:
        print(rock)
    if chosen == 1:
        print(paper)
    if chosen == 2:
        print(scissors)

def winner(chosen,comp):
    if chosen == comp:
        print("draw")
    elif (chosen == 1 and comp == 0) or (chosen == 2 and comp == 1) or (chosen == 0 and comp == 2):
        print("you won")
    else:
        print("you lost")


choose(rock,paper,scissors,chosen)
choose(rock,paper,scissors,comp)
winner(chosen,comp)
