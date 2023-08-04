
# this is the "test/stocks_test.py" file...

from app.stocks import format_usd, fetch_stocks_data

from pandas import DataFrame



def test_usd_formatting():

    assert format_usd(4.5) == "$4.50"

    assert format_usd(4.5555555) == "$4.56"

    assert format_usd(1234567890) == "$1,234,567,890.00"

    #assert format_usd("OOPS") == "______"



def test_data_fetching():
    result = fetch_stocks_data("NFLX")
    # it should return a dataframe:
    assert isinstance(result, DataFrame)
    # ... with specific columns:
    assert "timestamp" in result.columns
    assert "adjusted_close" in result.columns
    assert "high" in result.columns
    assert "low" in result.columns
    # ... with 100 rows, representing the latest trading days:
    assert len(result) >= 100


    #result = fetch_stocks_data("OOPS")
    # todo: test invalid inputs. what should happen?