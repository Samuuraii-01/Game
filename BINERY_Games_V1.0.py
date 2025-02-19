import random
import time

print("Hi, this is [snips, paper, stone Game]")
num = int(input("Enter The Number of your Turn Do you Want to play [ 3 , 5 , 7 , 9 , 11 ]: "))
point_H = 0
point_C = 0

if num not in [3, 5, 7, 9, 11]:
    print("Your Select Turn Is Wrong")
else:
    for i in range(num):
        while True:
            a = time.time()
            Human_Select = int(input("Enter your Select [ 1 to snips , 2 to paper , 3 to stone ]= "))
            b = time.time()
            c = b - a

            if Human_Select < 1 or Human_Select > 3:
                print("Your Select Subject Is Wrong")
                continue

            if c > 30:
                print("Do you think it's chess?")
                continue

            Computer_Select = random.randint(1, 3)
            print('point_C =', point_C, 'point_H =', point_H, "sel_c =", Computer_Select, "sel_H =", Human_Select)

            if Computer_Select == Human_Select:
                print("IT'S A TIE. Let's choose again.")
            else:
                break

        if Computer_Select != Human_Select:
            if (Computer_Select == 1 and Human_Select == 2) or (Computer_Select == 2 and Human_Select == 3) or (Computer_Select == 3 and Human_Select == 1):
                print("computer win")
                point_C += 1
            else:
                print("human win")
                point_H += 1

    print("Final Score - Computer:", point_C, "Human:", point_H)

    if point_C > point_H:
        print("COMPUTER wins the game!")
    elif point_C < point_H:
        print("YOU win the game!")
    else:
        print("The game is a tie!")
