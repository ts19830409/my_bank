import pytest
from src.generators import transaction_descriptions
from src.generators import filter_by_currency
from src.generators import card_number_generator


def test_filter_by_currency_correct(sample_transactions):
	"""Проверка фильтрации по валюте USD"""
	result = list(filter_by_currency(sample_transactions, "USD"))
	assert len(result) == 1

def test_filter_by_currency_no_matches(sample_transactions):
	"""Проверка на отсутствие транзакций в валюте GBP"""
	result = list(filter_by_currency(sample_transactions, "GBP"))
	assert result == []

def test_filter_by_currency_empty_list():
	"""Проверка на пустой список"""
	result = list(filter_by_currency([], "USD"))
	assert result == []

def test_transaction_descriptions_multiple():
	"""Проверка корректности описания для нескольких транзакций"""
	transactions = [
        {"description": "Перевод организации"},
        {"description": "Оплата услуг"},
        {"description": "Пополнение счета"}
    ]
	result = list(transaction_descriptions(transactions))
	assert result == ["Перевод организации", "Оплата услуг", "Пополнение счета"]


def test_transaction_descriptions_single():
	"""Проверка одной транзакции"""
	transactions = [{"description": "Единственная операция"}]
	result = list(transaction_descriptions(transactions))
	assert result == ["Единственная операция"]


def test_transaction_descriptions_empty():
	"""Проверяем пустой список"""
	result = list(transaction_descriptions([]))
	assert result == []

@pytest.mark.parametrize(
	"start_num, end_num, expected",
    [
	    (1, 5, [
		 "0000 0000 0000 0001",
	     "0000 0000 0000 0002",
	     "0000 0000 0000 0003",
	     "0000 0000 0000 0004",
	     "0000 0000 0000 0005"
		])
    ]
)

def test_card_number_generator(start_num, end_num, expected):
	"""Проверка на корректность"""
	result = list(card_number_generator(start_num, end_num))
	assert result == expected
	
@pytest.mark.parametrize(
	"start_num, end_num, expected",
	[
		(-5, -3, [
		 "0000 0000 0000 0005",
	     "0000 0000 0000 0004",
	     "0000 0000 0000 0003",
	    ])
	]
)
def test_card_number_generator_negative_values(start_num, end_num, expected):
	"""Проверка на корректность с отрицательными числами"""
	result = list(card_number_generator(start_num, end_num))
	assert result == expected

@pytest.mark.parametrize("args", [(), (1,), (1, 2, 3)])
def test_card_number_generator_wrong_arguments(args):
	"""Проверка на отсутствие аргументов"""
	with pytest.raises(TypeError):
		card_number_generator(*args)


def test_card_formatting():
	"""Проверка на корректность формата"""
	numbers = [1, 12, 123, 1234, 12345]
	for num in numbers:
		result = list(card_number_generator(num, num))
		card = result[0]
		
		assert len(card) == 19
		assert card.count(" ") == 3
		assert all(len(part) == 4 for part in card.split(" "))
		assert card.replace(" ", "").isdigit()


@pytest.mark.parametrize("start,end,expected_count", [
	(9999999999999990, 9999999999999999, 10),
	(0, 9, 10),
	(10000, 10000, 1),
])
def test_card_boundary_values(start, end, expected_count):
	"""Проверка на крайние значения и переходы"""
	result = list(card_number_generator(start, end))
	assert len(result) == expected_count


def test_generator_completion():
	"""Проверка на корректность завершение генератора"""
	gen = card_number_generator(1, 1)
	assert next(gen) == "0000 0000 0000 0001"
	with pytest.raises(StopIteration):
		next(gen)
		