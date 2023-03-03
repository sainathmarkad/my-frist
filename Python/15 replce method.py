                     # replace method
sainath = "sainathmarkad"                     
# replace method madhe aapan ekhad nav mhanje eka navachya jagevar aapan dusare nav gheu shakato
string = "she is beautifull and she is good dance"  #aapan string chya jagevar dusare kontehi nav gheu shakato
print(string.replace("is","was",1)) #yethe aaplyala double nav aasel tar aaplyala ek nav suddha replace karta yete tyacha number takun.

                     # find method
                    
# find method me hum string madhlya ekhadya word ki positipon pata kar sakte he 
a_pos1 = sainath.find("a") 
a_pos2 = string.find("a",a_pos1 + 1) # jar aaplyala dusrya number chi position pahije aasel tar hi method vapravi 
print(a_pos2)