l1=['sejal','savran',30,4.56]  #list defination
print(l1)   #print statement

l2=['my name is sejal']

l=l1+l2  #concatination
print(l)


#program to merge two list and sort it

l1=[10,28,98,76]
l2=[98,56,34,43]
new=l1+l2
print(new)
new.sort()
print(new)

#program to find largest number in a list
l1=[12,87,34,20,89]
#using sort
l1.sort()
print("Largest number in given list is : ",l1[-1])

#using max function
l2=max(l1)
print(l2)


#program to swap the furst and las value of a list
l1=[98,2,45,23,34]
temp=l1[0]
l1[0]=l1[-1]
l1[-1]=temp

print(l1)

#program to find list of even and odd number from given list
l=[12,56,74,34,23,89,65]
even=[]
odd=[]

for i in l:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("List of even numbers: ",even)
print("List of odd numbers: ",odd)


#program to find sum of all elements in a list
l1=[1,4,56,72,34]
total=0
i=0
while(i<=len(l1)):
    total+=l1(i)
    i+=1
print("Sum of all the elements given in list is : ",total)


