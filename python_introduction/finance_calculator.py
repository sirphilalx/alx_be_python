monthly_income = int(input('Enter your monthly income: '))
monthly_expense = int(input('Enter your total monthly expenses: '))

monthly_savings = monthly_income - monthly_expense

print(f'your monthly savings are ${monthly_savings}')

projected_savings = round(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f'Projected savings after one year, with interest, is: ${projected_savings}')