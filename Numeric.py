#swap two numbers using temporary variable
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
temp=a
a=b
b=temp
print("Values after swapping",a,b)

#swap two numbers without using temporary variable
A=int(input("Enter first number: "))
B=int(input("Enter second number: "))
A=A+B
B=A-B
A=A=B
print("Values after swapping",a,b)

#program for computing area and circumference of circle
R=int(input("Enter radius: "))
pi=3.14
circumference=2*pi*R
print(circumference)


#program fro note denomination in 2000, 500 and 100
amt=int(input("Enter amount: "))
TT=amt//2000
temp=amt%2000
FH=temp//500
temp=FH%500
H=temp//100
print("No. of two thousands notes:",TT)
print("No. of five hundred notes:",FH)
print("No. of one hundred notes:",H)

#program to find simple interest
p=int(input("Enter principle: "))
t=int(input("Enter time: "))
r=int(input("Enter rate: "))
si=(p*r*t)/100
print(si)


#program to calculate the total and average of 5 sub marks
H=int(input("Enter hindi marks: "))
E=int(input("Enter english marks: "))
M=int(input("Enter maths marks: "))
C=int(input("Enter chemistry marks: "))
P=int(input("Enter physics marks: "))

total=H+E+M+C+P
average=(total)/5
print(total)
print(average)

#program tofind length of longest member in give list
inp=int(input("enter no of elements : "))
li=[]
for xyz in range(0,inp):
    ele=input("enter element: ")
    li.append(ele)
    
max1=len(li[0])
max_ele=li[0]

for ele in li:
    if(len(ele) >max1):
        max1=len(ele)
        max_ele=ele
    print("length of longest elemwnt is : ",max1)
    print("longest element in given list is: ",ele)




    s1='Name: sejal,Adress:kherki daula'
l=s1.split(':')
print(l[-1])




s1='Name: sejal,Adress:kherki daula'
flag=0
re=''
for check in s1:
    if(check==':'):
        flag+=1
    if(flag==2):
        if(check==','):
            flag+=1
        else:
            re=re+check
print("adress of the user: ",re[1:])




s1='name:sejal savran,pan:hdj6746,adress:kherki daula,state:haryana'
flag=0
re=''
for check in s1:
    if(check==":"):
        flag+=1
        continue
    if(flag==3):
        if(check==","):
            break
        else:
            re=re+check
print("address: ",re)