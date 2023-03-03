            # number guessing game 
# winning_number = 8
# user_input = input("guese a number between 1 to 100 : ")
# user_input = int(user_input)
# if user_input == winning_number:
#     print("YOU WIN !!!!")
# else:
#     if user_input < winning_number:
#         print("too low ")    
#     else: 
#         print("too high") 
        
          #  number guessing modify
import random
winning_number = random.randint(1,100)  #pahile aapan variable ghetl  * ya madhe aapan import random ghetlyamule adjest number yeto
guess = 1 # he aapan kiti keles try kel te dakhavnyasathi he ariable ghetl
number = int(input("Guess a number b/t 1 to 100 : "))
game_over = False
while not game_over:
   if number == winning_number:    # if condition user ne number barobar guess kela ka chukicha guass kela te pahnyasathi
       print(f"you win, and you this number in {guess} time ")
       game_over = True
   else:
       if number < winning_number:
           print("to low")
           guess += 1
           number = int(input("guess again : "))
       else:
           print("too high")
           guess += 1
           number = int(input("guess again : "))    
