#!/usr/bin/python3
def perform_operation(num1, num2, operation):
    """a function that performs basic arithmetic operations"""
    if operation == 'divide':
        if num2 == 0:
            return 'division by zero is not supported'
        else:
            return num1 / num2
    elif operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    else:
        return 'unsupported operation'