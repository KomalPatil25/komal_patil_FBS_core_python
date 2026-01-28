try :
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operator = input("Enter operators (+,-,*,/): ")

    if operator not in ['+', '-', '*', '/']:
        raise ValueError('Invalid operator! Please choose correct.')
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError('Can not divided by zero!')
        result = num1 / num2
    print(f'Result: {num1} {operator} {num2} = {result}')

except ValueError as e:
    print('ERROR: ', e)

except ZeroDivisionError as e:
     print('ERROR: ', e)

except Exception as e:
     print('ERROR: ', e)