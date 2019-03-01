# cook your code here
print("hello world") #say hello

print("Simple Calculator") #Title of this Program
num1 = float(input("Enter your first number: "))  #Ask for first operator
op = input("Enter your operator (+,-,/,*,):  ")   #Ask For operator
num2 = float(input("Enter your second number: ")) #Ask for second

#If/else statement to determine the operator and case if invalid one is entered

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else: 
    print("Invalid operator")
