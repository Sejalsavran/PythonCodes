
#program to replace any particular character from given string with another character
s1=input("Enter string: ")
re=input("enter replace var: ")
ne=input("new var: ")

for i in s1:
    if(re==i):
        print(ne)
    else:
        print(i)

      
# program for encryption

str=input("Enter string: ")
enc1=''
for ch in str:
    ch=ord(ch)+1
    ch=chr(ch)
    enc1=enc1+ch
    
print(enc1)



#program for decryption

denc1=''
for ch in str:
    ch=ord(ch)-1
    ch=chr(ch)
    denc1=denc1+ch
    
print(denc1)


#program to print all number in a range divisible by a given no.

lower=int(input("Enter lower limit: "))
upper=int(input("Enter upper limit: "))
N=int(input("Enter number to be divided by: "))

for i in range(lower,upper):
    if(i%N==0):
        print(i)


#count length of any string without using any library function
str=input("Enter string: ")
count=0
for i in str:
    count+=1
    
print(count)


#print character and alpha. in given string
Str1=input("Enter string: ")

for i in Str1:
    print(i)