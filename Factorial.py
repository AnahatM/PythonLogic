
# DEFINE FUNCTION
def find_factorial(n):

	factorial = 1

	for i in range(1, n+1):
		 factorial *= i

	return factorial

print('\n')
p = 10
for i in range(1, p+1):

	print(find_factorial(i))

while True:

	try:
		num = int(input('Enter a number for which you want the factorial: '))
		
		if num == 0:
			print('The factorial of 0 is 1')
			quit()

		elif num < 0:
			print('Factorials do not exist for negative numbers. ')
			quit()

		elif num > 0:
			break

	except:
		print('-------------------------')

print(find_factorial(num))

