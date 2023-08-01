# "test/unemployment_test.py"

from app.unemployment import format_pct


def test_to_pct():

    # it formats percent sign, and rounds to two decimal places:

    assert format_pct(3.65554) == "3.66%"

    result = format_pct(25.4)
    assert result == '25.40%'