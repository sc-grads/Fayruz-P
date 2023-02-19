import openpyxl

wb = openpyxl.load_workbook('store.xlsx', data_only=True)

print(wb.sheetnames)

for sheet in wb:
    print(sheet.title)

sheet = wb['Products']
sheet = wb.active

b2_cell = sheet['B2']
c2_cell = sheet['c2']

print(b2_cell.value, c2_cell.value)

print(sheet.cell(row=4, column=2).value)

print(c2_cell.row, c2_cell.coulmn)

print(sheet['A5'].data_type)
print(sheet['B5'].data_type)
print(sheet['A5'].encoding)

print(sheet['D4'].parent)

print(dir(b2_cell))

# Reading data in a cell range
cell_range = sheet['B2:C11']
for product, price in cell_range:
    print(f'Product:{product.value}  Price:{price.value}')

print(f'Sheet Dimensions: {sheet.dimensions}')
print(sheet.max_row, sheet.max_column)

for a, b, c, d, e in sheet[sheet.dimensions]:
    print(a.value, b.value, c.value, d.value, e.value)

for row in sheet.rows:
    for cell in row:
        print(f'{cell.value}', end='')
    print('\n')

for row in sheet.values:
    print(row)
    