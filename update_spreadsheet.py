import openpyxl
from main import extract_game_info
import sys
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

def update_spreadsheet(filepath):
    # load workbook
    workbook = openpyxl.load_workbook("C:/Users/kylve/OneDrive/Documents/RL_Scrims_Summer_2024.xlsx")

    # select Games worksheet
    sheet = workbook["Games"]

    # find the current table
    table = next(iter(sheet._tables.values()))

    if table is None:
        print("Table could not be found")

    # extract the new row to be added
    new_row = extract_game_info(filepath)

    next_row = table.ref.split(':')[1][2:]
    if (int(next_row) > 1):
        next_row = int(next_row) + 1
    next_row = int(next_row)

    for col_num, value in enumerate(new_row, start=1):
        sheet.cell(row=next_row, column=col_num, value=value)

    # Update the table's reference
    end_col_letter = get_column_letter(len(table.tableColumns))
    table.ref = f"{table.ref.split(':')[0]}:{end_col_letter}{next_row}"

    # Save the workbook
    workbook.save("C:/Users/kylve/OneDrive/Documents/RL_Scrims_Summer_2024.xlsx")

if len(sys.argv) < 1:
    print("Invalid number of args given. Make sure you are only providing the path to the image you want scanned.")
    sys.exit(1)

update_spreadsheet(sys.argv[1])