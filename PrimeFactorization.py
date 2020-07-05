# PrimeFactorization.py


def prime_factorize(n):
	p = 2
	prime_factors = []
	while n >= p*p:
		if n%p == 0:
			prime_factors.append(int(p))
			n = n/p
		else:
			p += 1
			
	
	prime_factors.append(int(n))	
	print(f'There are {len(prime_factors)} prime factors.')
	print(f'{prime_factors}')

print('Welcome to Prime Factorization pro 3000')
print('What integer do you want to prime factorize?')

n = 0

# TAKING N INPUT
while True:
	try:
		while n <= 0:
			n = int(input('> '))
		break
		
	except:
		print('ERROR - Try Again...')

prime_factorize(n)



