import random

outcomes = []
tails = 0
heads = 0

def flip_coin():
    
    global tails
    global heads
    
    n = random.randint(1,2)
    
    if n == 1:
        heads += 1
        outcomes.append('Heads')
    
    elif n == 2:
        tails += 1
        outcomes.append('Tails')



while True:
    
    try:
        times = int(input('How many times do you want to flip a coin?'))
        break

    except:
        print('There was an error.')

for x in range(times):
    flip_coin()

print(f'Number of tails {tails}')
print(f'Number of heads {heads}')
print(outcomes)