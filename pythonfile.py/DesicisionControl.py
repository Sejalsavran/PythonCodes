#program to check wether an integer is positive or negative
N=int(input("Enter any integer: "))
if(N>=0):
    print("Positive")
else:
    print("Negative")


#program to take input of 5 subjects marks from user and display grades acordingly
H=int(input("Enter hindi marks: "))
E=int(input("Enter english marks: "))
M=int(input("Enter maths marks: "))
C=int(input("Enter chemistry marks: "))
P=int(input("Enter physics marks: "))

per=(H+E+M+C+P)/5
if(per>=90 and per<=100):
    print("A")
elif(per>=80 and per<90):
    print("B")
elif(per>=70 and per<80):
    print("C")
else:
    print("D")


#program to check wether a year is leap year or not
Year=int(input("Enter any year: "))
if(Year%4==0):
    print("Leap yaer")
else:
    print("common year")   


#program to check wether a number is even or odd
N=int(input("enter any number: "))
if(N%2==0):
    print("even")
else:
    print("odd")

#program to check greater no. among three numbers
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
if(n1>n2 and n1>n3):
    print("n1 is greater")
elif(n2>n1 and n2>n3):
    print("n2 is greater")
else:
    print("n3 is greater")


#program to take input of 3 sub from user and check marks individually if all are greater than 35-pass o/w fail
H=int(input("Enter hindi marks: "))
E=int(input("Enter english marks: "))
M=int(input("Enter maths marks: "))

if(H>35 and E>35 and m>35):
    print("Pass")
else:
    print("Fail")