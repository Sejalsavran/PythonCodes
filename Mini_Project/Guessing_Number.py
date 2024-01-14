import random


count=1
my_num=random.randint(1,100)
Guess_num=int(input("Guess nay number from 1 to 100. Enter -1 to EXIT."))
while Guess_num != -1:
   
    if Guess_num==-1:
        break

    elif Guess_num > 100 and Guess_num < 1:
        print("Invalid number.")
    elif Guess_num > my_num:
        print("It's greater. Try again!")
    elif Guess_num < my_num:
        print("It's smaller. Try again!")
    else:
        print("Congratulations!!!!!!!!You won.")







