# PrimeFactorization2.py
# Doing exactly what algorithm is saying

n = int(input('Input n'))

p = 2

print(f'{n} = ')

while n >= p*p:
	if n % p == 0:
		print(f'{p} *')
		n = n/p
	else:
		p = p+1

print(n)