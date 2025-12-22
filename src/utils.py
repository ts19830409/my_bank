import json
import logging
import os

from src.log_helper import create_file_handler

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = create_file_handler("utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_json_file(file_path) -> list:
    """Функция принимающая на вход JSON-файл и возвращающая список словарей
    с данными о финансовых транзакциях"""
    logger.debug(f"Начало загрузки JSON-файл {file_path}")
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                parsed_data = json.load(f)
                logger.debug(f"Загружаем JSON-файл {file_path}")
                if not isinstance(parsed_data, list):
                    logger.error(f"Данные в JSON-файле {file_path} не являются списком")
                    return []
            logger.info(f"JSON-файл {file_path} успешно загружен: {len(parsed_data)} элементов")
            return parsed_data

        except json.JSONDecodeError:
            logger.error(f"JSON-файл {file_path} имеет не верный формат")
            return []
    else:
        if not os.path.exists(file_path):
            logger.error(f"JSON-файл не найден: {file_path}")
        else:
            logger.error(f"JSON-файл пустой: {file_path}")

        return []
