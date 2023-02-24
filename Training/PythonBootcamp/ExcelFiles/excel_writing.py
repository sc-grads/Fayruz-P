import openpyxl

wb = openpyxl.load_workbook('store.xlsx')
sheet = wb.active

# sheet['D2'] = 400
# new_product = (11, 'Tablet', 12, 600, 12*600)
# sheet.append(new_product)

for c, d, e in sheet['c2:e12']:
    e.value = c.value * d.value

wb.save('store.xlsx')