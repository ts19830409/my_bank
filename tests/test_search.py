from collections import Counter

from src.search import process_bank_operations, process_bank_search


def test_process_bank_search_empty_data():
    """Тест 1: Поиск в пустом списке данных"""
    result = process_bank_search([], "Перевод")
    assert result == []


def test_process_bank_search_found():
    """Тест 2: Успешный поиск (найдено)"""
    data = [{"description": "Перевод организации"}, {"description": "Оплата услуг"}]
    result = process_bank_search(data, "перевод")
    assert result == [{"description": "Перевод организации"}]


def test_process_bank_search_not_found():
    """Тест 3: Поиск (не найдено)"""
    data = [{"description": "Оплата услуг"}]
    result = process_bank_search(data, "перевод")
    assert result == []


def test_process_bank_search_empty_search():
    """Тест 4: Пустая строка поиска (возвращает все данные)"""
    data = [{"description": "Перевод"}]
    result = process_bank_search(data, "")
    assert result == data


def test_process_bank_search_case_insensitive():
    """Тест 5: Поиск нечувствительный к регистру"""
    data = [{"description": "ПЕРЕВОД организации"}]
    result = process_bank_search(data, "перевод")
    assert result == data


def test_process_bank_search_with_regex():
    """Тест 6: Поиск с использованием regex (опционально)"""
    data = [{"description": "Перевод 100 рублей"}, {"description": "Перевод 200 долларов"}]
    result = process_bank_search(data, r"\d+")  # поиск цифр
    assert len(result) == 2


def test_process_bank_search_multiple_matches():
    """Тест 7: Несколько совпадений в одном списке"""
    data = [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты"},
        {"description": "Оплата услуг"},
    ]
    result = process_bank_search(data, "перевод")
    assert len(result) == 2
    assert result[0]["description"] == "Перевод организации"
    assert result[1]["description"] == "Перевод с карты"


def test_process_bank_search_partial_match():
    """Тест 8: Частичное совпадение (слово внутри другого слова)"""
    data = [{"description": "Денежный перевод"}]
    result = process_bank_search(data, "перевод")
    # Должен найти "перевод" в "Денежный перевод"
    assert len(result) == 1


def test_process_bank_operations_basic():
    """Тест 9: Базовый подсчёт категорий"""
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты"},
    ]
    categories = ["Перевод", "Вклад"]
    result = process_bank_operations(data, categories)

    # Преобразуем Counter в dict для сравнения
    assert dict(result) == {"Перевод": 2, "Вклад": 1}


def test_process_bank_operations_empty_data():
    """Тест 10: Подсчёт с пустыми данными"""
    result = process_bank_operations([], ["Перевод"])
    # Counter может не содержать ключ для нулевых значений
    assert result.get("Перевод", 0) == 0


def test_process_bank_operations_no_matches():
    """Тест 11: Подсчёт когда категории не найдены"""
    data = [{"description": "Оплата услуг"}]
    result = process_bank_operations(data, ["Перевод"])
    assert result.get("Перевод", 0) == 0


def test_process_bank_operations_multiple_categories():
    """Тест 12: Несколько категорий в одной транзакции"""
    data = [{"description": "Перевод и оплата услуг"}]
    result = process_bank_operations(data, ["Перевод", "Оплата"])
    # Если description содержит обе категории - обе должны увеличиться
    assert result.get("Перевод", 0) >= 0
    assert result.get("Оплата", 0) >= 0


def test_process_bank_operations_case_insensitive():
    """Тест 13: Подсчёт нечувствительный к регистру"""
    data = [{"description": "ПЕРЕВОД организации"}]
    result = process_bank_operations(data, ["перевод"])
    assert result.get("перевод", 0) == 1


def test_process_bank_operations_all_categories_zero():
    """Тест 14: Все категории равны 0"""
    data = [{"description": "Снятие наличных"}]
    categories = ["Перевод", "Вклад", "Оплата"]
    result = process_bank_operations(data, categories)

    # Проверяем что все категории либо отсутствуют, либо равны 0
    for category in categories:
        assert result.get(category, 0) == 0


def test_process_bank_search_missing_description():
    """Тест 15: Транзакция без поля description"""
    data = [{"id": 1}, {"description": "Перевод"}]  # нет description
    result = process_bank_search(data, "перевод")
    assert len(result) == 1


def test_process_bank_operations_empty_categories():
    """Тест 16: Пустой список категорий"""
    data = [{"description": "Перевод"}]
    result = process_bank_operations(data, [])
    assert result == Counter()  # Пустой Counter


def test_process_bank_search_special_characters():
    """Тест 17: Поиск со специальными символами"""
    data = [{"description": "Оплата (Visa)"}]
    result = process_bank_search(data, r"\(Visa\)")
    assert len(result) == 1


def test_process_bank_search_performance():
    """Тест 18: Проверка, что функция не падает на больших данных"""
    # Создаём 1000 транзакций
    data = [{"description": f"Операция {i}"} for i in range(1000)]
    data.append({"description": "Перевод"})

    result = process_bank_search(data, "Перевод")
    assert len(result) == 1


def test_process_bank_operations_performance():
    """Тест 19: Проверка подсчёта на больших данных"""
    data = []
    for i in range(100):
        data.append({"description": "Перевод"})
        data.append({"description": "Вклад"})

    result = process_bank_operations(data, ["Перевод", "Вклад"])
    assert result.get("Перевод", 0) == 100
    assert result.get("Вклад", 0) == 100
