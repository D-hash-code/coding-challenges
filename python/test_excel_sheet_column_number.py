from python.excel_sheet_column_number import titleToNumber


def test_title_to_number():
    INPUT_OUTPUT = [("A", 1), ("AB", 28), ("ABC", 731)]
    for (i, o) in INPUT_OUTPUT:
        func_out = titleToNumber(i)
        assert o == func_out
