import openpyxl
wb = openpyxl.Workbook()

sheet = wb.active

sales = {2017:700000, 2018: 800000, 2019: 900000}

sheet['A1'] = 'Year'
sheet['B1'] = 'Sales'

for k,v in sales.items():
    sheet.append((k,v))

wb.save('sales.xlxs')
