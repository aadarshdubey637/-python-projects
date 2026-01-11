# Game for losing and wining
import random
'''
1 for snake  
-1 for water
0 for gun'''

computer=random.choice([-1,0,1])
youstr=input("Enter Your Choice :")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

you =youdict[youstr]

print(f"Your Chose {reversedict[you]}\n Computer Chose {reversedict[computer]}")

if(computer==you):
    print("It's a Draw!")

else:
    if(computer==-1 and you == 1):
        print("You Win!")
    elif(computer==-1 and you == 0):
        print("You Lose!")
    elif(computer==1 and you == -1):
        print("You Lose!")
    elif(computer==1 and you == 0):
        print("You Win!")
    elif(computer==0 and you == -1):
        print("You Win!")
    elif(computer==0 and you == 1):
        print("You lose!")
    else:
        print("somthing went wrong")

