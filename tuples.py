#program to find the repeated items of a tuple item is given by user
tup=(2,4,3,4,2,5,5,4,3,2)
n=int(input("enter the digit for which u want to check: "))
count1=tup.count(n)
print(count1)


#program to checkwether an element exists within a tuple or not
tup=(2,4,3,4,2,5,5,4,3,2)
n=int(input("enter the digit u want to checkfor existence: "))
print(n in tup)


#program to covert a tuple into list
tup=(12,34,23,56)
abc=list(tup)
print(abc)
[12, 34, 23, 56]


#program to delete any element from tuple
tup1=(13,45,67,34)
N=int(input("Enter the element you want to delete: "))
tup2=list(tup1)
tup2.replace(N)
tup3=tuple(tup2)
print(tup3)



#Write a Python program to convert a tuple to a string.
tuple_3 = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)