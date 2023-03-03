    # show ticket printing
name = input("Enter your name is : ")  
age = input("please enter your age : ")
print("Name : "  + name)  
age = int(age)


if age==0 or age < 0:
    print("you can't watching")
 
elif 0<age<=3: 
    print("ticket price : free  ")

elif 3<age<=10:
    print("Ticket price : 150 ")
    
elif 10<age<=60:
    print("Ticket price : 250  ")
    
else:
    print("Ticket price : 200 ") 
    
    
      