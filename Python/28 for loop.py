# For loop with tange function
i = 1
for i in range(1,11):  #in range he nav khup mahatwche aahe 
    print(f"hello world {i}")  # aapan "i" chya jagevar dusre kuthle hi nav kivwa centax gheu shakato.
    #jar aaplyala navchya pudh number 0 pasun pahije aasel tar for loop vaparava.
# ha cod run zalyavar yachi range hi '0' pasun chalu hote  v '9' paryant sampte tyasathi "in range (1,11)" kelyavar
# barobar 1 te 10 paryant print hote 

      # example
      
total = "0"
total = int(total)
for i in range(1,11):
    total += i
print(total)


        #example 2
num = input("enter the number : ")
num = int(num)  # yethe aaplaya number ha integar madhe lagto mhanun aapan tyala khali "int" lavle aahe.
total = 0
for i in range(1,num+1):
    total += i
print(total)