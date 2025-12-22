import csv
import os

import pandas as pd


def load_csv_file(file_path) -> list:
    """Функция принимающая на вход csv-файл и возвращающая список словарей
    с данными о финансовых транзакциях"""
    transactions = []
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            with open(file_path, "r", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file, delimiter=";")
                for row in reader:
                    transactions.append(row)
                return transactions
        except csv.Error:
            return []
        except Exception:
            return []
    else:
        return []


def load_xlsx_file(file_path) -> list:
    """Функция принимающая на вход xlsx-файл и возвращающая список словарей
    с данными о финансовых транзакциях"""
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            df = pd.read_excel(file_path)
            result = df.to_dict("records")
            return result
        except Exception:
            return []
    else:
        return []
