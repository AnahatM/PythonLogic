# MULTIPLICATION TABLES .PY

# INPUT ONE
while True:

	try:
		first_input = int(input('How many tables do you want? '))
		break
	except:
		print('INVALID. ENTER AN INTEGER.')
# INPUT 2
while True:

	try:
		second_input = int(input('Ho long do you want each table to be? '))
		break
	except:
		print('INVALID. ENTER AN INTEGER.')

# DO THE PRINTING
for x in range(first_input+1):
	for y in range(second_input+1):
		print(f'{x} x {y} = {x*y}')

	print('\n')