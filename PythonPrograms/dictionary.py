dic1={'a':123,"b":321,'c':"python",'d':45.6}
dic2=dic1['b'],dic1['c']
print(dic2)
dic3=dic1['b'],dic1['c']=dic2=dic1['c'],dic1['b']
print(dic3)



#program to remove the given key from a dictionary
d1={'a':12,'b':34,'c':45,'d':1}
n=(input("enter the key you want to delete: "))
del(d1[n])
print(d1)




#program to multiply all the values in dictionary
inp=int(input("enter no of elements: "))
d={}
for xyz in range(0,inp):
    d[xyz+1]=int(input("enter value of key: "))
    
print("updated dictionary",d)
mul=1
for key in d:
    mul=mul*d[key]
print("Multiplication of all values: ",mul)    


#Write a Program to Check if a Given Key Exists in a Dictionary or Not.

dic1={'a':123,"b":321,'c':"python",'d':45.6}
key=input("Enter key for which you want to check: ")
if key in dic1.keys():
    print("Key is present in dict.")
    print(dic1[key])
else:
    print("Element is not present in dictionary")


#Write a Program to Concatenate Two Dictionaries Into One.

dic1={'a':123,"b":321,'c':"python",'d':45.6}
dic2={'c':432,"d":876,'c':"java",'d':87.5}
dic1.update(dic2)
print(dic1)

#Write a Python script to print a dictionary where the keys are numbers between 1 and 10 (both included) and the values are square of keys.

d=dict()
for i in range(1,10):
    d[i]=i**2
print(d)

