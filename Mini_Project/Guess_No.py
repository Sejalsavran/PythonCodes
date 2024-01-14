import random
num=random.randint(1,10)
guess=None

while guess != num:
    guess=int(input("Guess the number from 1 to 10: "))

    if guess==num:
        print("Congratulations!!!!! You won.")
        break
    elif guess>num:
        print("OOPS!It's greater, Try again.")
    else:
        print("OOPS!It's smaller, Try again.")
