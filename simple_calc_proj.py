#calculator proj 


def add(x,y): 
    return x + y

def subtract(x,y): 
    return x - y

def multiply(x,y): 
    return x * y

def divide(x,y):
    return x / y

opperation = input("What opperation would you like to use?(Add, Subtract, Multiply, Devide): ") 
num1 = float(input("Choose your first number: "))
num2 = float(input("Choose second number: "))

if opperation == "add": 
    print(f"The result is {add(num1,num2)}")
elif opperation == "subtract": 
    print(f"The result is {subtract(num1,num2)}")
elif opperation == "multiply": 
    print(f"The result is {multiply(num1,num2)}")
elif opperation == "divide": 
    if num2 == "0":
        print("Error, division by 0 is not aloud")
    else: 
        print(f"The result is {divide(num1,num2)}")
else: 
    print("invalid opperation")
