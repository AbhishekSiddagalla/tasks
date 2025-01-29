
from parsing_data import parsing_date

def test_valid_date():
    file_name = "NAV Portfolio Notebook_ELEQUIN INVESTMENTS, LLC_11052024.XLSX"
    expected_output = "Nov-05-2024"
    result = parsing_date(file_name)
    assert  result == expected_output

def test_valid_date_with_multiple_dates():
    file_name = "NAV Portfolio Notebook_ELEQUIN INVESTMENTS, LLC03102002_11052024.XLSX"
    expected_output = "Mar-10-2002"
    result = parsing_date(file_name)
    assert  result == expected_output

def test_without_date():
    file_name = "NAV Portfolio Notebook_ELEQUIN INVESTMENTS, LLC_ABCDEFGH.XLSX"
    expected_output = "Date Not Found"
    result = parsing_date(file_name)
    assert  result == expected_output

def test_with_numbers_exceeding_date_range():
    file_name = "NAV Portfolio Notebook_ELEQUIN INVESTMENTS, LLC_55229999.XLSX"
    expected_output = "Invalid Date"
    result = parsing_date(file_name)
    assert  result == expected_output


