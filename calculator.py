print("hey i am practicing in python")
up = input("Enter an opration (+ , - , * , /):")

if up in ['+', '-', '/', '*']:
    n1 = float(input("Enter first number:"))
    n2 = float(input("Enter second number:"))

#   adiition

    if up == '+':
        result = n1 + n2

#  subtraction  

    elif up == '-':
        result = n1 - n2

#  division

    elif up == '/':
        if n2 != 0:
            result = n1 / n2
        else:
            result = "error division by zero"
        
# multiplication  
  
    elif up == '*':
        result = n1 * n2


print(f"your result is: {result}")


