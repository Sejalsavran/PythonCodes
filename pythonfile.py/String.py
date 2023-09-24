#take a string and replace every blank space with a hyphen
str="my name is sejal savran"
newStr=str.replace(" ","_")
print(newStr)


#program to swap first character with last character
str1="sejal savran"
str2=str[0]
str3=str[-1]
str4= str1[-1]+str1[1:len(str1)-1]+str1[0]
print(str4)

#program to replace all "@"with "$"

S="sdh@gdh#@hh@df@Ghhs@@@sh@"
S2=S.replace("@","$")
print(S2)

#program to calculate no of characters in a string
s="sejal savran"
s1=len(s)
print(s1)

#program to count any particular character in given string
n="shififhirdfgihbci"
#this is to find "i" from this string
n1=n.count("i")
print(n1)

#program to split the string given by the user by the space
name="sejal savran"
newName=name.split(" ")
print(newName)