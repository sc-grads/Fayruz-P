#################################
## Working with Excel Files in Python
## The OpenPyXL Module
## Working with Styles
#################################

## Importing the module
import openpyxl

## Importing everything from the styles submodule
from openpyxl.styles import *

## Importing copy() function from copy module to copy styles
from copy import copy

## Loading an excel file. store.xlsx is in the same directory with the python script
wb = openpyxl.load_workbook('store.xlsx')

## Getting a sheet
sheet = wb['Products']

## Getting a cell by address. It will be modified
my_cell = sheet['B4']

## Printing all available styles
# print(dir(openpyxl.styles))

## Changing and setting a new font
font = Font(name='Tahoma', size=16, color=colors.RED, bold=True, italic=True, strike=False)
my_cell.font = font

## Setting a Pattern Fill
fill = PatternFill(fill_type='solid', fgColor=colors.YELLOW)
my_cell.fill = fill

## Setting cell border
double_border_green = Side(border_style='double', color=colors.GREEN)
thin_border_red = Side(border_style='thin', color='FF0000')
my_cell.border = Border(left=double_border_green, right=thin_border_red, top=double_border_green,
                        bottom=thin_border_red)

## Setting cell's content alignment
alignment = Alignment(horizontal='right', vertical='center')
my_cell.alignment = alignment

## Copy styles from a cell to another
new_cell = sheet['B10']
new_font = copy(my_cell.font)
new_font.color = colors.GREEN
new_cell.font = new_font

## Saving the changes
wb.save('store.xlsx')