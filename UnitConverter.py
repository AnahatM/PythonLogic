#UnitConverter.py

"""
> Ask category: temp, weight, volume, currency
> Ask what the amount is
> Ask what to covert it to
> If it is valid, convert it
> Return the answer
"""

print('Welcome to the Unit Converter!\n')
print('The categories are: ')
print('temperature, currency, volume, and mass.')

# LIST OF VALID CATEGORIES
valid_categories = ['temperature', 'currency', 'volume', 'mass']
print('What category do you want to convert from? ')
category = input("> ")

def pound_to_usd(pound):
	print(f'{pound} to usd = {1.22 * pound}')

def usd_to_pound(usd):
	print(f'{usd} to pound = {usd/1.22}')


# GET CATEGORY
while category not in valid_categories:
	print('INVALID CATEGORY')
	print('\n')
	print('What category do you want to convert from? ')
	category = input("> ")

if category == 'temperature':

	valid_temp = ['farenheit', 'celcius']
	print('What is original unit? (farenheit or celcius)')
	temp = input('> ')

	while temp not in valid_temp:
		print('INVALID UNIT')
		temp = input('Try Again > ')

	while True:
		try:	
			amount = float(input(f'What is the {temp} degree quantity?'))
			break
		except:
			print('There was an error. ')

	if temp == 'celcius':
		conversion = (9/5)*amount + 32
		print(f'{amount} celcius = {conversion} farenheit.')
	if temp == 'farenheit':
		conversion = (amount-32)*(5/9)
		print(f'{amount} farenheit = {conversion} celcius.')


if category == 'currency':
	
	valid_currency = ['pound', 'USD']

	print('What is the original unit? (pound, USD, Indian Ruppee)')
	currency = input('> ')

	while currency not in valid_currency:
		print('INVALID INPUT')
		currency = input('> ')

	while True:
		try:	
			amount = float(input(f'What is the {currency} amount?'))
			break
		except:
			print('There was an error. ')	

	if currency == 'pound':
		pound_to_usd(amount)

	else:
		usd_to_pound(amount)



if category == 'volume':
	pass

if category == 'mass':
	pass