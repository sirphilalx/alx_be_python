num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operation = input('Choose the operation (+, -, *, /):')

match operation:
    case '+':
        result = num1 + num2
        print(f'The result is {result}')
    case '-':
        result = num1 - num2
        print(f'The result is {result}')
    case '*':
        result = num1 * num2
        print(f'The result is {result}')
    case '/':
        if(num1 == 0 or num2 == 0):
            result = 'Cannot divide by zero.'
            print(result)
        else:
            result = num1 / num2
            print(f'The result is {result}')
    case _:
        result = 'enter a valid operator'
        print(result)