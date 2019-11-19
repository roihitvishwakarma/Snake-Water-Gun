import random
print("Welcome to the game")
print("press w for water,press g for gun,press s for snake")
u=0
c=0
d=0
i=0
for i in range(1,11):
    print("round",i)
    lst=["water","gun","snake"]
    choices=random.choice(lst)
    k=choices
    inp=input("enter input\n")
    if(inp=="w"):
        if(k=="water"):
            print("This round is draw\n")
            d=d+1
        elif(k=="gun"):
            print("You win this round\n")
            u=u+1
        else:
            (k=="snake")
            print("Computer win this round\n")
            c=c+1
    elif(inp=="g"):
        if(k=="water"):
            print("Computer win this round\n")
            c=c+1
        elif(k=="gun"):
            print("This round is draw\n")
            d=d+1
        else:
            (k=="snake")
            print("You win this round\n")
            u=u+1
    elif(inp=="s"):
        if(k=="water"):
            print("You win this round\n")
            u=u+1
        elif(k=="gun"):
            print("Computer win this round\n")
            c=c+1
        else:
            (k=="snake")
            print("This round is draw\n")
            d=d+1
    elif (i==2):
        print("Game over\n")
        #print("Result")
        #print("User point is:",u)
        #print("Computer point is:",c)
        #print("Draw matches:",d)
    else:
        print("You entered wrong argument other than s,w,g")
