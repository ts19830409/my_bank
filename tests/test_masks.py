import pytest

from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("700079228960636126", "Не верно введен номер карты"),
        ("70007922896063", "Не верно введен номер карты"),
        ("b000792 89606361", "Не верно введен номер карты"),
        (" ", "Не верно введен номер карты"),
        ("", "Не верно введен номер карты"),
    ],
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("73654108430135874305", "**4305"),
        ("73654108430135874", "Не верно введен номер счета"),
        ("73654108430135874305111", "Не верно введен номер счета"),
        ("7365410843015874 3s5", "Не верно введен номер счета"),
        (" ", "Не верно введен номер счета"),
        ("", "Не верно введен номер счета"),
    ],
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
