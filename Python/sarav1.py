# print("this is \\\\ double backlash ")
# print("this is /\\/\\/\\/\\/\\/ mountain")
# print("he is \t awesome (use escape sequence instead of manual space) ")
# print(" \\\" \\n \\t \\\'")
# print("line A \nline B")
            #   practices 2
# number1 = input("enter first number")
# number2 = input("enter second number") #long cut
# number3 = input("enter third number")
# number1,number2,number3 = (input("enter three numbers").split(",")) # ha shortcut aahe
# print((int(number1) + int(number2) + int(number3)) / 3)
# print(f"average of three number : {(int(number1) + int(number2) + int(number3)) /3}")
            # practices 3
# name = input("enter your name")            
# print("revers my name"[-1:-6:-2])
# print(f"revers of your name is{name}" )

            # while loop 
            # exercise 4    1

# user = input("enter a number : ")
# user = int(user)
# total = 0
# m = 1
# while m <= user:
#     total += m
#     m +=1
# print(total)

                #   2  
# number = ("enter a number : ")
# total = 0  # ya madhe aapan string chi berij karu shakato
# i = 0
# while i < len(number):
#    total += int(number[i])
#    i += 1
# print(total)
 
               # 3
name = input("enter your name : ") #aaplyala 'sainath markad' ya navamadhle ek ek
#aakshar kiti kiti vela aalel aahe te kadhayach aahe 
# "Sainath Markad"  *tar aaplyla khalil pramane lihava lagto 
# name.count("S") , name.count(name[0])
# name.count("A")  , name.count(name[1])
# name.count("I") , name.count(name[2])
# name.count("N") , name.count(name[3])
# name.count("T") , name.count(name[4])
# name.count("H") , name.count(name[5])
# name.count(" ") , name.count(name[6])
# name.count("M") , name.count(name[7])
# name.count("R") , name.count(name[8])
# name.count("K") , name.count(name[9])
# name.count("D") , name.count(name[10])
tem_variable = ""
i = 0   # yamadhe aaplyala eka navamadhe ek aakshar kiti vela aalel aahe te panyasathi aahe.
while i < len(name):
   if name[i] not in tem_variable:
      tem_variable += name[i]
   print(f"{name[i]} : {name.count(name[i])}")
   i += 1
  
  
       