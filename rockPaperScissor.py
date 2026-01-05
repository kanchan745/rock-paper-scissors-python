import random
class RockPaperScissors:
 def __init__(self):
    self.choice = ["rock","paper","scissors"]
 def play(self):
     user = input("Enter rock paper or scissors: ").lower()
     computer = random.choice(self.choice)
     
     print("Computer chose: ",computer)
     
     if user == computer:
         print("It is a Tie!")
     elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer =='paper'):
         print("You Win!!!!!")
     else:
         print("Computer Wins!!!!!")    

game = RockPaperScissors()
game.play()                             