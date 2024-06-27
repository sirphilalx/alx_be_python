num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operator = input('Choose the operation (+, -, *, /):')

match operator:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if(num1 == 0 or num2 == 0):
            result = 'Cannot divide by zero.'
        else:
            result = num1 / num2
    case _:
        result = 'enter a valid operator'

print(result)