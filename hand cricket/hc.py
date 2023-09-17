import math
import random


def play(status,compstatus):
    huscore=0;
    coscore=0;
    while True:
        uturn=int(input("Enter your turn(type: 1 to 6):"))
        if(uturn>6):
            print("Please enter in range between 1 to 6 ")
        compturn=math.ceil(random.random()*6)
        if(uturn==compturn):
            print("OUTT..........")
            return huscore,coscore
            break
        else:
            if(status=="bat"):
                huscore=huscore+uturn
                print("Human score:",huscore)
            else:
                coscore=coscore+compturn
                print("Computer Score:",coscore)


print("--------Hello Welcome to Hand Cricket Game-------")
pri=input("Odd or Even (type ODD or EVEN):")
print(pri)
if(pri=="ODD"):
    comp_pri="EVEN"
else:
    comp_pri="ODD"
toss=int(input("Toss podunga boss'ae (type 1 to 6):"))
comp_toss= math.ceil(random.random()*6)
print("Your turn is ",toss)
print("Computer turn is ",comp_toss)
restoss=comp_toss+toss

tothuscore=0
tocoscore=0

if((restoss%2==0 and comp_pri=="EVEN") or (restoss%2!=0 and comp_pri=="ODD")):
    print("Computer won tne toss!")
    
    compstatus='bat'
    status='bowl'
    print("You are "+status+"\'ing man")
    print("Computer is "+compstatus+"\'ing")
    hscore,coscore=play(status,compstatus)
    
    tothuscore=tothuscore+hscore
    tocoscore=tocoscore+coscore
    
    print("Now you are batsman!")
    
    compstatus='bowl'
    status='bat'
    hscore,coscore=play(status,compstatus)

        
    tothuscore=tothuscore+hscore
    tocoscore=tocoscore+coscore

    
else:
    print("You won the toss!")
    status=input("Enter Batting or Bowling( type :bat or bowl):")
    if(status=='bat'):
        compstatus='bowl'
    print("You are "+status+"\'ing man")
    print("Computer is "+compstatus+"\'ing")
    
    hscore,coscore=play(status,compstatus)

            
    tothuscore=tothuscore+hscore
    tocoscore=tocoscore+coscore
    
    if(status=="bat"):
        status='bowl'
        compstatus='bat'
    hscore,coscore=play(status,compstatus)

            
    tothuscore=tothuscore+hscore
    tocoscore=tocoscore+coscore
    
print("Highest score of human is : ",tothuscore)
print("Highest score of computer is  : ",tocoscore)


if(tothuscore>tocoscore):
    print("You are win! Congratulations")

else:
    print("Better luck next time! Computer is won!")

