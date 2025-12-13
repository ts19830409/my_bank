from unittest.mock import Mock, patch
from src.external_api import convert_to_rub

def test_rub_transaction():
	"""Тест на корректность данных в рублях"""
	transaction = {
		"operationAmount": {
			"amount": "1000",
			"currency": {"code": "RUB"}
		}
	}
	result = convert_to_rub(transaction)
	assert result == 1000.0


def test_usd_transaction_with_mock():
	"""Тест на транзакцию в валюте"""
	# Создаем фейковый ответ API
	fake_response = Mock()
	fake_response.status_code = 200
	fake_response.json.return_value = {"result": 7500.0}
	
	with patch('src.external_api.requests.get', return_value=fake_response):
	
		with patch('src.external_api.os.getenv', return_value="fake_key"):
			transaction = {
				"operationAmount": {
					"amount": "100",
					"currency": {"code": "USD"}
				}
			}
			result = convert_to_rub(transaction)
			assert result == 7500.0


def test_api_error():
	"""Тест на ошибки от API"""
	fake_response = Mock()
	fake_response.status_code = 401
	
	with patch('src.external_api.requests.get', return_value=fake_response):
		with patch('src.external_api.os.getenv', return_value="fake_key"):
			transaction = {
				"operationAmount": {
					"amount": "100",
					"currency": {"code": "EUR"}
				}
			}
			result = convert_to_rub(transaction)
			assert result == 0.0


def test_no_api_key():
	"""Тест на отсутствие API_KEY"""
	with patch('src.external_api.os.getenv', return_value=None):
		transaction = {
			"operationAmount": {
				"amount": "100",
				"currency": {"code": "USD"}
			}
		}
		try:
			convert_to_rub(transaction)
			assert False, "Ошибка!"
		except ValueError as e:
			assert "API_KEY" in str(e)