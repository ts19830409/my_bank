def filter_by_currency(transactions, currency_code):
	"""Функция возвращает транзакции, где валюта операции соответствует заданной"""
	for transaction in transactions:
		if transaction["operationAmount"]["currency"]["code"] == currency_code:
			yield transaction
	

def transaction_descriptions(transactions):
	"""Функция принимает список словарей с транзакциями и возвращает описание операции"""
	for transaction in transactions:
		yield transaction["description"]
	
	
def card_number_generator(start, end):
	"""Функция принимает начальное и конечное значения для генерации диапазона номеров"""
	for num in range(start, end + 1):
		module_of_numbers = abs(num)
		quantity_of_characters = len(str(module_of_numbers))
		quantity_of_zeros = 16 - quantity_of_characters
		number_without_spaces = (quantity_of_zeros * '0') + str(module_of_numbers)
		correct_format = [number_without_spaces[i:i + 4] for i in range(0, len(number_without_spaces), 4)]
		new_correct_format = " ".join(correct_format)
		yield new_correct_format
	