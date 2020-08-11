import ezsheets


def check_sum_table(first_column, second_column, sum_column, spreadsheet):
    """Check sum of 2 values from 2 columns."""
    ss = ezsheets.Spreadsheet(spreadsheet)
    number_of_rows = ss[0].rowCount
    for row in range(2, number_of_rows+1):
        if ss[0].getRow(row)[0] == '':
            print(f"no more rows to check!\nlast checked row: {row}")
            break
        if not int(ss[0].getRow(row)[first_column]) * int(ss[0].getRow(row)[second_column]) == int(ss[0].getRow(row)[sum_column]):
            print(
                f"wrong sum in row: {row}. "
                f"{int(ss[0].getRow(row)[sum_column])} is not equal: "
                f"{int(ss[0].getRow(row)[first_column])} * "
                f"{int(ss[0].getRow(row)[second_column])}")


if __name__ == '__main__':
    check_sum_table(0, 1, 2, '1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
