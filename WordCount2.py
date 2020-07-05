my_string = input('Enter a string: ')

count = 0

separators = [' ', '.', ',', '-']

for letter in my_string:
	if letter in separators:
		count += 1

while my_string[0] in separators or my_string[-1]:
	count -= 1


print(count)	