# IS THE NUMBER IN A LIST?

while True:
    try:
        length = int(input('How many items do you want in your list?'))
        break
    except:
        print('There was an error, try again.')
        print('========================================')

list = []

for i in range(length):

    try:
        answer = int(input('Enter a number for the list: '))
        list.append(answer)
    except:
        print('ERROR, TRY AGAIN')
        print('=================================================')
        

print('===========================================')
while True:
    try:
        n = int(input('For what number do you want to see whether or not it in in the list? '))
        break
    except:
        print('ERROR, TRY AGAIN')
        print('======================================================')

if n in list:
    print('Yes')
else:
    print('No')