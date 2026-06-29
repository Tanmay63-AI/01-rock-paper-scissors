import random

print("\nWe are going to play ROCK PAPER SCISSOR")
print("\nPress\nr for Rock\np for Paper\ns for Scissor")

l = []
youDict = { "r":-1, "p":0, "s":1 }
reverseDict = { -1:"Rock", 0:"Paper", 1:"Scissor" }

for i in range(5):

    computer = random.choice([-1,0,1])
    youStr = input(f"\n Enter choice {i+1}: ")
    you = youDict[youStr]

    print(f" You choose {reverseDict[you]}\n Computer choose {reverseDict[computer]}")

    if ( computer == you ):
        print(" It's a Draw!\n")
        l.insert(i,"d")
    
    else:
        if ( computer == -1 and you == 0 ):
            print(" You Won!\n")
            l.insert(i,"w")
        
        elif ( computer == -1 and you == 1 ):
            print(" You Lose!\n")
            l.insert(i,"l")

        elif ( computer == 0 and you == -1 ):
            print(" You Lose!\n")
            l.insert(i,"l")

        elif ( computer == 0 and you == 1 ):
            print(" You Won!\n")
            l.insert(i,"w")

        elif ( computer == 1 and you == -1 ):
            print(" You Won!\n")
            l.insert(i,"w")

        elif ( computer == 1 and you == 0 ):
            print(" You Lose!\n")
            l.insert(i,"l")
        
        else:
            print(" Something went wrong.\n")
        
if ( l.count("w") > l.count("l")):
    print(" You 'Won' the game!\n")

elif ( l.count("d") == 5 or l.count("w") == l.count("l")):
    print(" This game is Draw!\n")

else:
    print(" You 'Lose' the game!\n")
