def main():
    operation = input('''
Please type in a math equation using the following symbols:
"+" to add
"-" to subtract
"*" to multiply
"/" to divide
press enter to start equation
''')

    number1 = int(input('Please enter first number: '))
    number2 = int(input('Please enter second number: '))

    if operation == '+':
        print('{} + {} = '.format(number1, number2)) 
        print(number1 + number2)

    elif operation == '-':
        print('{} - {} = '.format(number1, number2)) 
        print(number1 - number2)

    elif operation == '*':
        print('{} * {} = '.format(number1, number2))
        print(number1 * number2)

    elif operation == '/':
        print('{} / {} = '.format(number1, number2)) 
        print(number1 / number2)

    else:
        print('why cant you do something right for once.')

main()