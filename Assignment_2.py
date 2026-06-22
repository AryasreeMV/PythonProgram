# Calculator program

# Taking two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Taking the operation to be performed from the user
op = input("Enter the operation to be performed: ")

# Comparing the operator and executing the corresponding arithmetic operation
if(op == "+"):
    print(num1, "+", num2, "=", num1+num2)
elif(op == "-"):
    print(num1, "-", num2, "=", num1-num2)
elif(op == "*"):
    print(num1, "*", num2, "=", num1*num2)
elif(op == "/"):
    print(num1, "/", num2, "=", num1/num2)
elif(op=="%"):
    print(num1, "%", num2, "=", num1%num2)
elif(op=="//"):
    print(num1, "//", num2, "=", num1//num2)
elif(op=="**"):
    print(num1, "**", num2, "=", num1**num2)
else:
    print("Invalid operator..!")


# Pattern printing

#Fetching user input for the number of rows
rows = int(input("Enter the number of rows : "))

# Looping through each row
for i in range(1, rows + 1):
    # Printing numbers in decreasing order for the current row
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()  # Moving to the next line after each row
