#program to calculate digits of a number

n=int(input("enter an integer number: "))
count=0
while(n>0):
    count=count+1
    n=n//10
print("Total digits of given number: ",count)


#program to calculate reverse of a number
n=int(input("enter an integer number: "))
rev=0
org=n
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10

print("reverse no: ",rev)
if(org==rev):
    print("mirror number")
else:
    print("not a mirror number")


#program to calculate fcatorial of a number
N1=int(input("Enter any number: "))
fact=1
i=1
while(i<=N1):
  fact=fact*i
  i=i+1
print("Factorial of a number is",fact)

#program to print table
n1=int(input("Enter a number: "))
i=1
while(i<=10):
    table=n1*i
    print(n1,"*",i,"=",table)
    i=i+1


#program to find out odd number from 0 to 100

i=0
while(i<=100):
    if(i%2==1):
        print(i)
    i=i+1


#power series
n=int(input("enter a positive integer: "))
print('1 ',end=' ')
a=2
while(a<=n):
    print("+1/",a,end='')
    a=a+1


#program to find sum of digits in a number
I=int(input("Enter any integer value: "))
tot=0
while(I>0):
    dig=I%10
    tot=tot+dig
    I=I//10
print("Sum of digits of given number is: ",tot)



    

