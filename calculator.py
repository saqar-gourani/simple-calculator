def add(a , b):
    return a+b

def subtract(a , b):
    return a-b

def multiply(a , b):
    return a*b

def divide(a , b):
    if b !=0:
        return a/b
    else:
        return "Error! division by zero"
    
print("simple calculator")    
print("1. Add\n2. subtract\n3. multiply\n4. Divide")

choice= int(input("Enter choice (1/2/3/4):"))
num1=float(input("Enter first number :"))
num2=float(input("Enter second number :"))

if choice==1 :
    print("result :" , add(num1 , num2))
elif choice==2:
    print("result :" , substract(num1 , num2))
elif choice==3:
    print("result :" , multiply(num1 , num2))  
elif choice==4:
    print("result :" , divide(num1 , num2))      
else:
    print("Invalid choice")    