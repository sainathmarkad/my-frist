# for loop sarav 3
# ya madhe aaplyala number input karaycha aahe pan input kelelya numer chi berij aali pahije
#mhanun khalil pramane
# :. samja number "1256" ghetla tar tyachi berij 14 aali paije 
# tyasathi aaplyala number ha string madhla intigear made pahije
# 1+2+5+6    aani output 14 aal pahije
num =  input("enter the number : ")
total = 0
for i in range(0,len(num)):
   total += int(num[i])
print(total)

    #  practices for loop 2
# ask user name and count each character
# "Sainath Markad"

name = input("Enter your name & number  : ")
temp = "" # he veriable empty thevaych karan 
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
    temp += name[i]