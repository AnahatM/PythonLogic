#SumOfNumbers.py
print('This will find the sum of all the numbers till the number you enter. ')
print('For Example: input = 9, answer = 1+2+2+3+4+5+...9')


num = int(input('Enter a number till which you want the sum of: '))
answer = (num * int((num+1))/2)
print('The sum of the numbers till', num, 'is', answer)
