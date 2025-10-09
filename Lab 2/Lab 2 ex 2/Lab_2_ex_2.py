'''
ex 2 lab 2
'''

##print("Inserati data nasterii (zi/luna/an)")

from datetime import datetime
from datetime import date

Present = datetime.today().strftime('%d %m %Y').split()
Present = date(int(Present[2]), int(Present[1]), int(Present[0]))

DateIN = input("Inserati data nasterii (zi/luna/an): ")
DateIN = DateIN.split("/")
DateIN = date(int(DateIN[2]), int(DateIN[1]), int(DateIN[0]))
print(f"Varsta persoanei este de {(Present - DateIN).days} zile")












'''
Present = datetime.today().strftime('%d %m %Y').split()


DateIN = input("Inserati data nasterii (zi/luna/an): ")
DateIN = DateIN.split("/")

ani = int(Present[2])-int(DateIN[2])
if(int(Present[1])<int(DateIN[1])):
    ani-=1
elif(Present[1] == DateIN[1]):
    if(int(Present[0])<int(DateIN[0])):
        ani-=1
        

print(f"Persoana are {ani} ani")
'''
