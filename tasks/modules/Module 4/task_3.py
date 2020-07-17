from pathlib import Path
import shutil
from pprint import pprint
from pyinputplus import inputStr


def copy_chosen_extension(file_type):
    """Find in a tree files with given extension and copy to chosen folder."""
    data_folder = Path(inputStr("Provide absolute path to tree parent folder: "))
    destination_folder = Path(inputStr("Provide absolute path to destination folder: "))
    files_in_folder = sorted(data_folder.rglob(f'*.{file_type}'))
    copied_files = []
    if not files_in_folder:
        return "No files with given extension in chosen folder"
    for file in files_in_folder:
        shutil.copy(file, destination_folder)
        copied_files.append(file)
    return copied_files


if __name__ == '__main__':
    chosen_files = copy_chosen_extension("pdf")
    pprint(chosen_files)
