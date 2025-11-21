import pytest


@pytest.fixture
def operations_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sort_data():
    return [
        {"date": "2023-01-15", "name": "A"},
        {"date": "2023-03-10", "name": "B"},
        {"date": "2023-02-05", "name": "C"},
    ]


@pytest.fixture
def simple_data():
    return [
        {"date": "2023-01-01", "name": "A"},
        {"date": "2023-02-01", "name": "B"},
    ]


@pytest.fixture
def invalid_data():
    return [
        {"date": "2023-01-01", "name": "A"},
        {"name": "B"},
    ]
