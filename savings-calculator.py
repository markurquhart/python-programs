'''Program that calculates savings and interest'''

initial_savings = int(input('Enter initial savings amount ($): '))
monthly_incremental = int(input('Enter monthly contribution ($): '))
interest_rate = float(input('Enter savings rate (%): '))/100
yearly_incremental = monthly_incremental * 12

years = int(input('Enter years: '))
print()

savings = initial_savings
for i in range(years):
    print(' Savings in year {}: ${:,.2f}'.format(i, savings))
    # this math should get us close to what annual, calculated once compound interest would be
    savings = savings + yearly_incremental + ((savings + yearly_incremental)*interest_rate)

print('\n')
