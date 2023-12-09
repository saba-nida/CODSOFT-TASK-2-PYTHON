print("--------------------CALCULATOR------------------")
print()
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
operator= str(input("Enter the operator: "))
if operator=='+':
    output1=num1+num2
    print("The sum of two numbers is: " ,output1)
elif operator=='-':
    output2=num1-num2
    print("The difference between two numbers is :",output2)
elif operator=='x':
    output3=num1*num2
    print("The product of two numbers is: ",output3)
elif operator == "/":
    output4=num1/num2
    print("The quotient after divinding two numbers is : ",output4)
elif operator =="%":
    output5= num1%num2
    print("The modulas is : ",output5)
else:
    print("Invalid operator")