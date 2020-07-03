"""Find string and replace.

Finds 'ADJECTIVE', 'NOUN', 'ADVERB', or 'VERB' occurrences in text file
and allows to replace them with chosen strings.
"""

from pathlib import Path
from re import search, sub
from pyinputplus import inputStr


# Program CONSTANTS
STRINGS_TO_FIND = [
    'ADJECTIVE', 'NOUN', 'ADVERB', 'VERB'
]


def mad_libs(file_path, list_of_patterns):
    """Search for pattern from list and replace with user's string."""
    path_to_rw_files = Path(file_path)
    with open(path_to_rw_files, 'rt') as my_file:
        text_file_content = my_file.read()
    for pattern in list_of_patterns:
        search_result = search(pattern, text_file_content)
        while search_result:
            replacement = inputStr(
                f'Enter new word to replace "{pattern}":')
            text_file_content = sub(
                pattern, replacement, text_file_content, count=1)
            search_result = search(pattern, text_file_content)
    print(text_file_content)
    with open(fr'{path_to_rw_files.absolute().parent}/{path_to_rw_files.stem}__CHANGED.txt', 'w') as new_text_file:
        new_text_file.write(text_file_content)


if __name__ == '__main__':
    mad_libs(
        'tasks/modules/Module 4/task_1_files/text_file.txt', STRINGS_TO_FIND)
