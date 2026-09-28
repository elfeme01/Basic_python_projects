# to import opnpyxl, i need to make sure i have add it in the terminal using 'pip install openpyxl'
# i use the (as xl) so i wont have to type openpyxl every time in the rest of the code
import openpyxl as xl
from openpyxl.chart import BarChart, Reference  # i add the chart diagrams

# i create the process_workbook so i can use this following by only changing the file name


def process_workbook(filename):
    wb = xl.load_workbook(filename)
    sheet = wb['Sheet1']  # in which sheet we are working on
    # cell = sheet['a1']  # this and the one bellow are exaclty the same
    # cell = sheet.cell(1, 1)

    # sheet.max_row counts all the rows, and i need to add +1 , to include the last row
    for row in range(2, sheet.max_row + 1):
        # so i call all the rows from colum 3 except the 1st one thats a string
        cell = sheet.cell(row, 3)
        # because i wanna lower each price by 10%
        corrected_price = cell.value * 0.9
        # i identify in which cells the corrected prices should go
        corrected_price_cell = sheet.cell(row, 4)
        # i assign the prices of the corrected shells
        corrected_price_cell.value = corrected_price

    values = Reference(sheet,
                       min_row=2,
                       max_row=sheet.max_row,
                       min_col=4,
                       max_col=4)  # I identify which cells its going to refer to by rows and colyms

    # i identify the chart , and i add the values i assigned above
    chart = BarChart()
    chart.add_data(values)
    # I identify where the chart is gonna be placed by giving it the starting cell
    sheet.add_chart(chart, 'e2')

    wb.save(filename)  # i save the changes in the xlsx file
