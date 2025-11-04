import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(full_string: str) -> str:
    """Функция обрабатывающая информацию о картах и счетах."""
    full_name = full_string.split()
    number = full_name[-1]
    if len(number) == 16:
        name = " ".join(full_name[:-1])
        number = get_mask_card_number(number)
        return f"{name} {number}"
    elif len(number) == 20:
        name = " ".join(full_name[:-1])
        number = get_mask_account(number)
        return f"{name} {number}"
    else:
        return "Введены не корректные значения"


def get_date(full_date_string: str) -> str:
    """Функция изменения формата даты"""
    full_date = re.split(r"T", full_date_string)
    new_date = full_date[0].split("-")
    return f"{new_date[2]}.{new_date[1]}.{new_date[0]}"
