# ChangeReturn.py

"""
The user enters a cost and then the amount of money given.
The program will figure out the change and the number of 
quarters, dimes, nickels, pennies needed for the change.
"""

while True:
    
    try:
        cost = float(input('What is the cost? '))
        break        
    except:
        print('There was an error, try again: ')


while True:
    
    try:
        given = float(input('What is the amount given? '))
        if given > cost or given == cost:
            break
        elif given < cost:
            print('You did not pay enough')

    except:
        print('There was an error, try again: ')
        


# RETURN CHANGE
change = (given - cost)
change = round(change, 2)
print(f'The change is {change}')

# Get quarters, dimes, nickels, and pennies

dollar = 100
q = 25
d = 10
n = 5
p = 1

dime = 0
nickels = 0
quarters = 0
pennies = 0

# Turn it all to cents
cents = change * 100


# Do division and get coin values
quarters = cents//q
cents -= 25*quarters # Get remainder
if cents != 0 and cents > 0:
    # get dimes
    dime = cents//d
    cents -= 10*dime # Get remainder again
    if cents != 0 and cents > 0:
        # Get nickels
        nickels = cents//n
        cents -= 5*nickels # Remainder
        if cents != 0 and cents > 0:
            # Get pennies
            pennies = cents

quarters = int(quarters)
dime = int(dime)
nickels = int(nickels)
pennies = int(pennies)

print(f'The coins for the change are {quarters} quarters, {dime} dimes, {nickels} nickels, and {pennies} pennies.')




