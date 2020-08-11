"""Checks files naming and renames if gaps present."""


from pathlib import Path
from re import search
import shutil
from pyinputplus import inputStr


def fill_the_gaps(prefix, file_type="txt"):
    """Fix indexes in files with same prefix in name."""
    path_to_folder = inputStr("Provide absolute path to folder: ")
    data_folder = Path(path_to_folder)
    files_in_folder = sorted(data_folder.rglob(f'{prefix}*.{file_type}'))
    if not files_in_folder:
        print("No files with given prefix and/or type in chosen folder")
        return
    number_len = len(search(r'\d+', files_in_folder[0].stem).group())
    sorting_number = int(search(r'\d+', files_in_folder[0].stem).group())
    for file in files_in_folder:
        file_index = int(search(r'\d+', file.stem).group())
        if file_index != sorting_number:
            changed_name_path = data_folder / f"{prefix}{sorting_number:0{number_len}d}.{file_type}"
            shutil.move(file, changed_name_path)
        sorting_number += 1

if __name__ == '__main__':
    fill_the_gaps("spam")
