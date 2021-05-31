'''Program that calculates savings and interest'''

initial_savings = 5000
monthly_incremental = 750
interest_rate = 0.05

years = int(input('Enter years: '))
print()

savings = initial_savings
for i in range(years):
    print(' Savings in year {}: ${:.2f}'.format(i, savings))
    savings = savings + (savings*interest_rate) + (monthly_incremental*12)

print('\n')
