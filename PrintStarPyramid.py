# STAR PYRMID.PY


while True:
    try:
        print('================================')
        print('How many rows do you want?')
        number = int(input('> '))
        break
    except:
        print('There was an error, try again:')

number_of_spaces = number

for x in range(number):
    x += 1
    print(' ' * number_of_spaces, 'X '*x)
    number_of_spaces -= 1

































































































