print('This will count vowells in a string.')
print('Enter a string: ')
string = input('> ')

vowells = ['a', 'e', 'i', 'o', 'u']
num = 0
answers = []

for letter in string:
    if letter in vowells:
        answers.append(letter)
        num += 1

a = 0
e = 0
i = 0
o = 0
u = 0

for vowell in answers:
    if vowell == 'a':
        a += 1
    elif vowell == 'e':
        e += 1
    elif vowell == 'i':
        i += 1
    elif vowell == 'o':
        o += 1
    elif vowell == 'u':
        u += 1
        
print(f'The string has {num} vowells.')
print(f' a = {a} | e = {e} | i = {i} | o = {o} | u = {u}')