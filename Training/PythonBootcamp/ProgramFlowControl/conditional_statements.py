# # Conditional Statements
#
balance = 100
price = 50

if balance >= price:
    answer = input('Do you want to continue? Enter yes or no:')
    answer = answer.lower()
    if answer == 'yes':
        print('We\'ll move on.')
    elif answer == 'no':
        print('We\' stop.')
    else:
        print('Invalid answer.')
    new_balance = balance + price
    print(f'You can book the flight and your new balance will be {new_balance}.')
else:
    print(f'Insufficient finds!Please deposit {price - balance}')


