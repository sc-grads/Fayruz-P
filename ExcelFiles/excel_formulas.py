import openpyxl
wb = openpyxl.load_workbook('store.xlsx')
sheet = wb.active
# sheet['e3'] = 'c3*d3'

for c, d, e in sheet['c2:e12']:
    e.value = f'={c.coordinate}*{d.coordinate}'
    

wb.save('store.xlxs')
