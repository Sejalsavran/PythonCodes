'''import math
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
r1=(-b + math.sqrt(b**2 - 4*a*c))/(2*a)
print(r1)'''


'''n=int(input("Enter number: "))


while n >0:
    r=n%10
    n=n//10
    print(r)'''

'''n=int(input("Enter no.: "))
i=0
while n>0:
    print(n,"*",i,'=',i*n)
    i+=1'''

'''n=int(input("Enter no.: "))
i=0
while n>0:
    n=n//10
    i+=1

print("number of digits: ",i)'''


'''n=int(input("Enter number: "))
i=0 
sum=0
while n>0:
    r=n%10
    n=n//10
    sum+=r
    i+=1
print(sum)'''


'''n=int(input("Enter number: "))

while n>=0:
    r=n%10
    n=n//10
    print(r)'''


#int sum of given number
'''num=int(input("Enter no. of digitd you want to add: "))

sum=0
count=0

while count <num:
    n=int(input("Enter numbers: "))
    sum+=n
    count+=1
print(sum)'''


#sum of positive and negitive number from given numbers
'''N=int(input("Enter how many numbers you want to enter: "))
count=0
psum=0
nsum=0
while count<N:
    num=int(input("Enter numbers: "))
    if(num>1):
        psum+=num
        
    else:
        nsum+=num
    count+=1
print("Sum of positive number: ",psum)
print("Sum of negative",nsum)'''


#reverse of a number

'''n=int(input("Enter number: "))
m=n
rev=0
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
print(rev)
print(n)

if m==rev:
    print("pelindrome")
else:
    print("not pelindrome")'''
    

 

    





