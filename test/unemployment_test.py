# "test/unemployment_test.py"

from app.unemployment import format_pct, fetch_unemployment_data


def test_to_pct():

    # it formats percent sign, and rounds to two decimal places:

    assert format_pct(3.65554) == "3.66%"

    result = format_pct(25.4)
    assert result == '25.40%'


def test_unemployment_data():

    data = fetch_unemployment_data()

    # it returns a list of dicts:
    assert isinstance(data, list)
    assert isinstance(data[0], dict)

    # where each has a "date" and "value":
    assert list(data[0].keys()) == ["date", "value"]

    # and rates are formatted as floats:
    assert isinstance(data[0]["value"], float)

    # including a full history since 1948
    assert len(data) >= 906
    #assert data[-1]["date"] == "1948-01-01"
    assert data[-1] == {'date': '1948-01-01', 'value': 3.4}



