#FindQuadrant.py

"""
> User enters x cor
> User enters y cor 
> do some if statements
> return quadrant

         |
   Q 2   |  Q 1
         |
++++++++++++++++++++
	     |
   Q 3   |  Q 4
	     |
"""

print('Welcome.')
print('This program will find which quadrant the point is in. ')
print('The quadrants look something like this:')

# Print grid
print('\n')
print('         |')
print('   Q 2   |  Q 1')
print('         |')
print('++++++++++++++++++++')
print('	 |')
print('   Q 3   |  Q 4')
print('	 |')

def	print_grid(x,y,boolean = True):
	
	if boolean:
		print('\n')
		print('         |')
		print('   Q 2   |  Q 1')
		print('         |')
		print('++++++++++++++++++++')
		print('	 |')
		print('   Q 3   |  Q 4')
		print('	 |')
	else:
		print('\n')
		print('         |')
		print('   Q 2   |  Q 1')
		print('         |')
		print('++++++++++++++++++++')
		print('	 |')
		print('   Q 3   |  Q 4')
		print('	 |')

# > Get x
while True:

	try:
		print('\n')
		print('Enter an x-coordinate: ')
		x = float(input('> '))
		break

	except:
		print('There was an error, try again. ')
	

# > Get y
while True:

	try:
		print('\n')
		print('Enter a y-coordinate: ')
		y = float(input('> '))
		break

	except:
		print('There was an error, try again. ')

print('\nPROCESSING...')

# Handle if statements
if x > 0 and y > 0:
	# (+,+)
	print('The point is in Quadrant I')

elif x < 0 and y > 0:
	# (-,+)
	print('The point is in Quadrant II')

elif x < 0 and y < 0:
	# (-,-)
	print('The point is in Quadrant III')

elif x > 0 and y < 0:
	# (+,-)
	print('The point is in Quadrant IV')

elif x == 0 or y == 0:

	if x == 0 and y != 0:
		print('Your point is on y-axis.')
	elif y == 0 and x != 0:
		print('Your point is on x-axis.')
	elif x==0 and y ==0:
		print('your point is on the origin.')
