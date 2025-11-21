import pytest
from src.processing import filter_by_state
from src.processing import sort_by_date

@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 2),
    ("PENDING", 0),
])
def test_filter_by_state(operations_data, state, expected_count):
    result = filter_by_state(operations_data, state)
    assert len(result) == expected_count

def test_filter_by_state_default(operations_data):
    result = filter_by_state(operations_data)
    assert len(result) == 2
    assert all(item['state'] == 'EXECUTED' for item in result)

def test_basic_functionality(sort_data):
    result = sort_by_date(sort_data, reverse=True)
    assert [item["date"] for item in result] == ["2023-03-10", "2023-02-05", "2023-01-15"]

def test_default_parameter(simple_data):
    result = sort_by_date(simple_data)
    assert result[0]["date"] == "2023-02-01"

def test_empty_list():
    result = sort_by_date([])
    assert result == []

def test_missing_date_key(invalid_data):
    with pytest.raises(KeyError):
        sort_by_date(invalid_data)