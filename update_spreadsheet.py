import openpyxl
from main import extract_game_info
import sys

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

    next_row = table.ref.split(':')[1][1:]
    next_row = int(next_row) + 1

    for col_num, value in enumerate(new_row, start=1):
        sheet.cell(row=next_row, column=col_num, value=value)

    # Update the table reference to include the new row
    table.ref = f"{table.ref.split(':')[0]}:{openpyxl.utils.get_column_letter(table._max_col)}{next_row}"

    # Save the workbook
    workbook.save("C:/Users/kylve/OneDrive/Documents/RL_Scrims_Summer_2024.xlsx")

if len(sys.argv) < 1:
    print("Invalid number of args given. Make sure you are only providing the path to the image you want scanned.")
    sys.exit(1)

update_spreadsheet(sys.argv[1])