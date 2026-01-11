'''
import random

computer=random.choice([-1,0,1])
youstr=input("Enter your choice :")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

you=youdict[youstr]

print(f"your choice {reversedict[you]}\n computer choice {reversedict[computer]}")
if(computer==you):
    print("Its a draw ")
else:
    if((computer==-1) or (you==1)):
       print("you win!")
    elif((computer==-1) or (you==0)):
      print("you lose!")
    elif((computer==1) or (you==-1)):
        print("you win!")
    elif((computer==1) or (you==0)):
        print(" you lose!")
    elif((computer==0) or (you==-1)):
        print("you lose!")
    elif((computer==-0) or (you==1)):
        print("you lose!")
    else:
        print("something went wrong !")
'''
        
import random

computer=random.choice([-1,0,1])
youstr=input("Enter your choice :")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

you=youdict[youstr]

print(f"your choice {reversedict[you]}\n computer choice {reversedict[computer]}")
if(computer==you):
    print("Its a draw ")
else:
    if((computer-you == 1) or (computer-you==-2)):
        print("you lose !")
    else:
        print("you win !")