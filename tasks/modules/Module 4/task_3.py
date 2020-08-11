import os
from pathlib import Path
import shutil
from pyinputplus import inputStr


def copy_chosen_extension(file_type):
    """Find in a tree, files with given extension and copy to chosen folder."""
    data_folder = Path(inputStr("Provide absolute path to tree parent folder: "))
    destination_folder = Path(inputStr("Provide absolute path to destination folder: "))
    os.makedirs(destination_folder, exist_ok=True)
    files_in_folder = data_folder.rglob(f'*.{file_type}')
    copied_files = []
    if not files_in_folder:
        print("No files with given extension in chosen folder")
        return
    for file in files_in_folder:
        shutil.copy(file, destination_folder)
        copied_files.append(file)


if __name__ == '__main__':
    copy_chosen_extension("pdf")
