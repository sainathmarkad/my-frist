                #   Break keywoard
                
# break keyword ko aapan loop la break karnyasathi use kartat. / loop la sampvnyasathi vapartat
# jar aaplyala 1 te 10 paryanta number print kale aani aaplayala te 5 var thambayche aahet tar 
          # hi method vapartat.
 
for i in range(1,11): # yamadhe 10 ghyaycha aahe mhanun 11 lihava 
                      #jo aakda ghyacha aahe tyachya pudhacha aakda chyava
    if i==5:
        break  # yamdhe break lihilyamule hi method yethe thambli.
    print(i)   # print 4 hote karan jo aakda lihila aahe tyachya aagodarcha aakda print.
    
    
print("____________________________")  # hi line timepass lihili aahe



                   # continue keyword
# ya method madhe continue mhanje 1 te 10 paryant print karayche aahe tyat ekhada aakda vaglaycha 
  # mhanje samja 5 nahi ghyayacha tyala continue method mhantnt
  # ex :- 1,2,3,4,6,7,8,9,10
for i in range(1,11):
    if i==5:
        continue  # he continue lavlyamulke hi methd ne 5 dilit kela 
    print(i)
    