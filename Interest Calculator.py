print('How many years will you be saving?')

while True:
    years = int(input('Enter number of years: '))
    if years in range(0,111):
        break
    elif years > 110:
        print('You are probably not gonna live that long. Please give a more reasonable value.')
    else:
        print('This is not a valid number of years. Try again.')

print('How much money is currently in your account?')
principal = float(input('Enter current amount in account: '))

print('How much do you plan on investing monthly?')
monthly_invest = float(input('Enter investing amount: '))

print('What do you estimate to be the yearly interest of this investment?')
while True:
    interest = float(input('Enter interest in % (ie 0-100): '))
    if interest in range(0,100):
        interest = interest/100
        break
    else:
        print('This is not a valid interest value. Try again.')

monthly_invest = monthly_invest*12

final_amount = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = principal
    
    final_amount = (final_amount + monthly_invest) * (1 + interest)

print(f'This is how much you would have after {years} years: ${final_amount}')
