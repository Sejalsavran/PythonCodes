#calculator
first_number=int(input("Enter first number: "))
second_number=int(input("Enter second number: "))
print("Press nay key for  operator(+,-,*,/): ")
operator=input("")
if(operator=="+"):
    print(first_number+second_number)
elif(operator=="-"):
    print(first_number-second_number)
elif(operator=="*"):
    print(first_number*second_number)
elif(operator=="/"):
    print(first_number/second_number)
else:
    print("invalid operation")