a = 10
b = 5
operation = "add"  

if operation == "add":
    result = a + b
elif operation == "subtract":
    result = a - b
elif operation == "multiply":
    result = a * b
elif operation == "divide":
    if b != 0:
        result = a / b
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"

print(result)
