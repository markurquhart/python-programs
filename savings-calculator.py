'''Program that calculates savings and interest'''

initial_savings = int(input('Enter initial savings amount ($): '))
monthly_incremental = int(input('Enter monthly contribution ($): '))
interest_rate = float(input('Enter savings rate (%): '))/100

years = int(input('Enter years: '))
print()

savings = initial_savings
for i in range(years):
    print(' Savings in year {}: ${:,.2f}'.format(i, savings))
    # this math indiciates interest that compounds on a yearly basis
    savings = savings + (monthly_incremental*12) + ((savings+(monthly_incremental*12))*interest_rate)

print('\n')
