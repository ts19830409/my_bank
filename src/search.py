import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция для поиска в списке словарей операций по заданной строке"""
    result_search = []
    if search == "":
        return data
    else:
        pattern = re.compile(search, re.I)
        for transaction in data:
            description = transaction.get("description", "")
            if pattern.search(description):
                result_search.append(transaction)
    return result_search


def process_bank_operations(data: list[dict], categories: list) -> dict[str, int]:
    """Функция для подсчета количества банковских операций определенного типа"""
    counter = Counter()
    for transaction in data:
        description = transaction.get("description", "")
        for category in categories:
            if re.search(category, description, re.I):
                counter[category] += 1
    return counter
