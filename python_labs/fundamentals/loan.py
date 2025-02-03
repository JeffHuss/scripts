money_owed = float(input('How much money do you owe, in dollars?\n'))
apr = float(input('What is the annual percentage rate of the loan?\n'))
payment = float(input('How much are your monthly payments?\n'))
months = int(input('How many months do you want to see the results for?\n'))


monthly_rate = (apr / 100) / 12

for i in range(months):
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid
    if (money_owed < payment):
        print('The last payment is', money_owed)
        print('You paid off the loan in', i + 1, 'months.')
        break
    money_owed = money_owed - payment

print('Paid', payment, 'of which', interest_paid, 'was interest.')
print('Now I owe', money_owed)