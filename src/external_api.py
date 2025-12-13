import os

import requests
from dotenv import load_dotenv


def convert_to_rub(transaction: dict) -> float:
    """Функция, принимающая на вход транзакцию и возвращающая сумму транзакции"""
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY не найден в .env файле")

    amount_user = transaction["operationAmount"]["amount"]
    currency_user = transaction["operationAmount"]["currency"]["code"]
    amount_user_convert = float(amount_user)

    if currency_user == "RUB":
        return amount_user_convert
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_user}&amount={amount_user_convert}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            api_data = response.json()
            amount_user_convert = api_data.get("result", 0.0)
            return round(amount_user_convert, 2)
        else:
            print(f"Ошибка: {response.status_code}")
            return 0.0
