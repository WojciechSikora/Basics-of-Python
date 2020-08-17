"""Find string and replace.

Finds 'ADJECTIVE', 'NOUN', 'ADVERB', or 'VERB' occurrences in text file
and allows to replace them with chosen strings.
"""

from pathlib import Path
import re
from pyinputplus import inputStr


def mad_libs(file_path):
    """Search for pattern from list and replace with user's input."""
    path_to_rw_files = Path(file_path)
    with open(path_to_rw_files, 'rt') as my_file:
        text_file_content = my_file.read()
    pattern = re.compile(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b')
    for match in pattern.finditer(text_file_content):
        replacement = inputStr(f'Enter new word to replace "{match.group(0)}":')
        text_file_content = re.sub(match.group(0), replacement, text_file_content, 1)
    print(f'Changed text:\n{text_file_content}')
    with open(fr'{path_to_rw_files.absolute().parent}/{path_to_rw_files.stem}__CHANGED.txt', 'w') as new_text_file:
        new_text_file.write(text_file_content)


if __name__ == '__main__':
    mad_libs(
        'tasks/modules/Module 4/task_1_files/text_file.txt')
