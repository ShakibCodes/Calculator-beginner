print("my calculator project")

up = input("Enter an operation (+ , - , / , *):")

n1 = float(input("Enter your first number:"))
n2 = float(input("Enter your second number:"))

if up in ['+', '-', '/' , '*']:

    if up == '+':
        result = n1 + n2

    elif up == '-':
        result = n1 - n2

    elif up == '/':
        if n2 != 0:
            result = n1 / n2
        else:
            result = "invalid relust division by 0"

    elif up == '*':
        result = n1 * n2

    else:
        print("Enter A vali operation")

print(f"your result is: {result}")