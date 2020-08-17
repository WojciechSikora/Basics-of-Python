from pathlib import Path
import csv
import os
import openpyxl
from pyinputplus import inputStr


def convert_excel_to_csv():
    """Take all excel files in provided dir and convert them to csv."""
    data_folder = Path(inputStr("Provide absolute path to folder with excel files: "))
    files_in_folder = data_folder.glob('*.xls*')
    if not files_in_folder:
        print("No files with given prefix and/or type in chosen folder")
        return
    csv_folder = Path(inputStr("Provide absolute path to destination folder(to save csv): "))
    os.makedirs(csv_folder, exist_ok=True)
    for file in files_in_folder:
        ss_name = file.stem
        wb = openpyxl.load_workbook(file)
        for sheet in wb.sheetnames:
            with open(csv_folder / f'{ss_name}_{sheet}.csv', 'w', newline="") as file:
                csv_instance = csv.writer(file)
                for row in wb[sheet].rows:
                    csv_instance.writerow([cell.value for cell in row])


if __name__ == '__main__':
    convert_excel_to_csv()
