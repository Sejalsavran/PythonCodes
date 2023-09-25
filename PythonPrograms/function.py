#program for encryption using function

def encryption(str1):
    enc1=''
    for ch in str1:
        ch=ord(ch)+1
        ch=chr(ch)
        enc1=enc1+ch
    print(enc1)    

str=input("Enter string: ")
encryption(str)



#program for decryption using function(with argument, without return type)

def decryption(str1):
    denc1=''
    for ch in str1:
        ch=ord(ch)-1
        ch=chr(ch)
        denc1=denc1+ch
    print(denc1)

strrr=input("enter string: ")
decryption(strrr)


#program to return largest elementin a list(without argument, with return type)
def return_largest():
    li=['abcdee','abcd','abc','ab']
    max_li=len(li[0])
    max_ele=li[0]
    
    for xyz in li:
        if max_li<=len(xyz):
            max_li=len(xyz)
            max_ele=xyz
    return max_ele
    
var=return_largest()
print("largest element: ",var)


#with argument and with return type
def return_largest(li):
    
    max_li=len(li[0])
    max_ele=li[0]
    
    for xyz in li:
        if max_li<=len(xyz):
            max_li=len(xyz)
            max_ele=xyz
    return max_ele
    
var=return_largest(['abcdee','abcd','abc','ab'])
print("largest element: ",var)





#length of string
def length(seq):
    len1=0
    for xyz in seq:
        len1+=1
    return len1
    
re1=length("sejal")
re2=length([12,23,45,66])
print(re1,re2)
print(len("sejal"),len([12,23,45,66]))


#Write a Program to take two input form user and make decision calculator using function.
def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def multiply(p,q):
    return p*q
def division(p,q):
    return p/q

choice=input("Enter a for addition, s for sub,M for multiplication and D for division: ")

num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))

if choice=='a':
    print("addition of given number: ",add(num_1,num_2))
elif choice=='b':
    print("subtraction of given number: ",sub(num_1,num_2))
elif choice=='c':
    print("multiplication of given number: ",multiply(num_1,num_2))
else:
    print("division of given numebr: ",division(num_1,num_2))
    