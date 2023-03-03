  # Don't repeat yourself
         # mhanje jar ekhadya cod madhe ek line dabal lihavi lagat aasel tar
                        # DRY principle vaparun ti lines sarya cod madhe ekdach lihai lagte
import random
winning_number = random.randint(1,100) #pahile aapan variable ghetl
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
       else:
           print("too high")
       guess += 1
       number = int(input("guess again : "))    # yethe aapan DRY principle vaparlel aahe.
       
