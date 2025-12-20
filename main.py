# from src.masks import get_mask_card_number, get_mask_account
# from src.utils import load_json_file
# import json
#
# # Тестируем masks
# print("Тестируем masks.py:")
# print(get_mask_card_number("1234567812345678"))
# print(get_mask_account("12345678901234567890"))
#
# # Тестируем utils
# print("\nТестируем utils.py:")
# test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
# with open("test.json", "w") as f:
#     json.dump(test_data, f)
#
# data = load_json_file("test.json")
# print(f"Загружено записей: {len(data)}")
#
# print("\nЛоги созданы в папке logs/")

# import csv
#
#
# with open("data/transactions.csv", "r", encoding="utf-8") as csv_file:
#     reader = csv.DictReader(csv_file, delimiter=';')
#     for row in reader:
#         print(row)


import pandas as pd

df = pd.read_excel("data/transactions_excel.xlsx")
print(df.shape)
print(df.head())
