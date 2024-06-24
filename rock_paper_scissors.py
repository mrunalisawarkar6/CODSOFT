import random 
rock = '''
       _ _ _ _ __
-----'    _ _ _ _)
          (_ _ _ _)
           (_ _ _ _)
          (_ _ _ _)
-----._ _(_ _ _ _)
'''

paper='''
         
        ---------,
 ------' _ _ _ _ _)_ _ _ _
         _ _ _ _ _ _ _ _ _) 
         _ _ _ _ _ _ _ _ _ )
         _ _ _ _ _ _ _ _ _)
-------- _ _ _ _ _ _ _ )

'''

scissors ='''

       ________
------'   _____)_________
           ______________)
           _______________)
          (________)
-------.___(_____)

'''

game_image =[rock,paper,scissors]
user_choice =int(input("Enter your Choice : (Type 0 for Rock,1 for Paper,2 for Scissors.)\n"))
if user_choice >= 3 or user_choice < 0:
    print("You entered invalid number.")
else:
  print(game_image[user_choice])
  computer_choice= random.randint(0,2)
  print("Computer Choose:")
  print(game_image[computer_choice])
  if computer_choice==user_choice:
    print("It's a draw.")
  elif computer_choice== 0 and user_choice ==2:
    print("You Lose.")
  elif user_choice == 0 and computer_choice==2:
    print("You Win.")
  elif computer_choice > user_choice:
    print("You Lose.")
  elif user_choice > computer_choice :
    print("You Win.")

