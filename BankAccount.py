"""
In this game, you manage a bank account...
"""

class Account:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print('Deposit accepted. Your balance is now ${}'.format(self.balance))
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print('Withdrawl accepted. Your balance is now ${}'.format(self.balance))
        else:
            print('[FUNDS UNAVIALABLE]')
            
            print('Your balance is ${}'.format(self.balance))
            
    def __str__(self):
        return f' ############# \n| Balance: {self.balance} \n| Owner: {self.owner} \n #############'

print('What is your name?')
name = input('> ')
print('How much money do you want to start with?')
balance = int(input('> '))

account = Account(name, balance)

print(account)

valid_inputs = ['withdraw', 'deposit', 'quit']

while True:
	print('\n Do you want to deposit money or withdraw money or [QUIT] ?')
	answer = input('> ')
	answer = answer.lower()

	if answer in valid_inputs:
		if answer == 'withdraw':
			print('How much do you want to withdraw? ')
			amount = int(input('> '))
			account.withdraw(amount)
		elif answer == 'deposit':
			print('How much miney do you want to deposit?')
			amount = int(input('> '))
			account.deposit(amount)
		elif answer == 'quit':
			print('[QUITTING]...')
			break

	else:
		print('Not a valid input. (Maybe check spelling?)')
		
