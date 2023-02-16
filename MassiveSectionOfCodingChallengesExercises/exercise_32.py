phone = {'Brand': 'Samsung', 'Price': 650.2, 'Seller': 'Nile'}

price = phone['Price']
vat = format(price * 0.19, '.2f')  # format() returns a string
vat = float(vat)  # casting to float

print(vat)



