def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает список словарей по ключу state"""
    list_operations = []
    for status in operations:
        if status.get("state") == state:
            list_operations.append(status)
    return list_operations


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортирует список словарей по дате"""
    list_sorted_date = sorted(operations, key=lambda operation: operation["date"], reverse=reverse)
    return list_sorted_date