import json
import os


def load_json_file(file_path) -> list:
	"""Функция принимающая на вход JSON-файл и возвращающая список словарей
	с данными о финансовых транзакциях"""
	if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
		try:
			with open(file_path, "r", encoding="utf-8") as f:
				parsed_data = json.load(f)
				if not isinstance(parsed_data, list):
					return[]
			return parsed_data
		
		except json.JSONDecodeError:
			return[]
	else:
		return[]
	