from pathlib import Path
import PyPDF4
from pyinputplus import inputStr


def decrypt_pdf():
    """Use words list from dictionary_file to decrypt pdf file."""
    path_to_dict = Path(inputStr("Provide absolute path to dictionary file: "))
    path_to_pdf = Path(inputStr("Provide absolute path to encrypted pdf file: "))
    with open(path_to_dict, 'rt') as my_file:
        dictionary = my_file.read()
    pdf_reader = PyPDF4.PdfFileReader(open(path_to_pdf, 'rb'))
    for word in dictionary.split():
        if pdf_reader.decrypt(word) == 1:
            print(f"Password found! It's: {word}")
            break
        elif pdf_reader.decrypt(word.lower()) == 1:
            print(f"Password found! It's: {word.lower()}")
            break


if __name__ == '__main__':
    decrypt_pdf()
