weight = input('Enter your weight in kg:')
height = input('Enter your height in m:')
bmi = float(weight) / (float(height) ** 2)
print('Your BMI is', format(bmi, ' .2f'))
