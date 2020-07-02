"""Task 2 from Module 3 - Basics-Of-Python."""


def my_split(string, separator=None):
    """Take 'string' and create list using 'separator'."""
    if separator is None:
        separator = " "
    if not isinstance(string, str):
        raise TypeError("Argument is not a string")
    if not isinstance(separator, str):
        raise TypeError("Separator is not a string")
    if not separator:
        raise ValueError("Separator is empty")
    start_index = 0
    end_index = 0
    list_from_string = []
    while string.find(separator) != -1:
        end_index = string.index(separator)
        list_from_string.append(string[start_index:end_index])
        string = string[end_index + len(separator):]
    list_from_string.append(string)
    return list_from_string
