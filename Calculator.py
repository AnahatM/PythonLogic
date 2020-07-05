# ScientificCalculator.py
print('Welcome to the Scientific Calculator!')
print('Operations are + - * / //  ^ and %')
print("="*10)
print('\n')

# GET FIRST NUMBER
while True:
    
    try:
        n1 = float(input('What is the first number? '))
        break        
    except:
        print('There was an error, try again: ')

# GET SECOND NUMBER
while True:
    
    try:
        n2 = float(input('What is the next number? '))
        break        
    except:
        print('There was an error, try again: ')

# ASK FOR OPERATOR

"""
> Create a list of valid operators
> Ask for input
> Keep asking until you get valid input
"""

valid_operations = ['*', '+', '/', '-', '//', '^', '%']


operation = input('What operation do you want?')

while operation not in valid_operations:
	print('INVALID OPERATION: ')
	operation = input('What operation do you want?')

# FIND THE RESULT
if operation == '+':
	print(f'{n1} + {n2} = {n1+n2}')
	# ADDING

elif operation == '-':
	print(f'{n1} - {n2} = {n1-n2}')
	# SUBTRACTION

elif operation == '*':
	print(f'{n1} * {n2} = {n1*n2}')
	# MULTIPLY

elif operation == '/':
	print(f'{n1} / {n2} = {n1/n2}')
	# DIVIDE

elif operation == '^':
	print(f'{n1} ^ {n2} = {n1**n2}')
	# EXPONENT

elif operation == '%':
	print(f'{n1} % {n2} = {n1%n2}')

elif operation == '//':
	print(f'{n1} // {n2} = {n1//n2}')
	# INT DIVISION