from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.transactions import load_csv_file, load_xlsx_file
from src.utils import load_json_file
from src.widget import get_date, mask_account_card


def main() -> None:
    """Основная функция программы"""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print(
        """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )

    choice = int(input())

    if choice == 1:
        print("Для обработки выбран JSON-файл.")
        data = load_json_file("data/operations.json")
        # print(data)
    elif choice == 2:
        print("Для обработки выбран CSV-файл.")
        data = load_csv_file("data/transactions.csv")
        # print(data)
    elif choice == 3:
        print("Для обработки выбран XLSX-файл.")
        data = load_xlsx_file("data/transactions_excel.xlsx")
        # print(data)
    else:
        print("Введено не верное число")

    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        status_choice = input().upper()
        if status_choice in ["EXECUTED", "CANCELED", "PENDING"]:
            data = filter_by_state(data, status_choice)
            print(f'Операции отфильтрованы по статусу "{status_choice}"')
            # print(data)
            break
        else:
            print(f'Статус операции "{status_choice}" недоступен.')

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        answer_sort = input().capitalize()
        if answer_sort == "Да":
            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                answer_sort_ascending = input().lower()
                if answer_sort_ascending == "по возрастанию":
                    data = sort_by_date(data, False)
                    break
                elif answer_sort_ascending == "по убыванию":
                    data = sort_by_date(data, True)
                    break
                else:
                    print('Введите "по возрастанию" или "по убыванию"')
            break
        elif answer_sort == "Нет":
            break
        else:
            print('Введите "Да" или "Нет"')

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        answer_sort_RUB = input().capitalize()
        if answer_sort_RUB == "Да":
            # data = filter_by_currency(data, "RUB")
            data = list(filter_by_currency(data, "RUB"))
            break
        elif answer_sort_RUB == "Нет":
            break
        else:
            print('Введите "Да" или "Нет"')

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        answer_sort_word = input().capitalize()
        if answer_sort_word == "Да":
            print("Введите слово для фильтрации")
            sort_word = input().lower()
            data = process_bank_search(data, sort_word)
            break
        elif answer_sort_word == "Нет":
            break
        else:
            print('Введите "Да" или "Нет"')

    # print(data)
    # print(f"Всего банковских операций в выборке: {len(data)}")
    def formatted_response(transaction: dict) -> str:
        formatted_date = get_date(transaction["date"])
        formatted_description = transaction["description"]

        from_masked = ""
        if "from" in transaction:
            from_masked = mask_account_card(transaction["from"])
        to_masked = mask_account_card(transaction["to"])

        amount_user = transaction["operationAmount"]["amount"]
        currency_user = transaction["operationAmount"]["currency"]["name"]

        if from_masked:
            return (
                f"{formatted_date} {formatted_description}\n"
                f"{from_masked} -> {to_masked}\n"
                f"Сумма: {amount_user} {currency_user}"
            )
        else:
            return (
                f"{formatted_date} {formatted_description}\n" f"{to_masked}\n" f"Сумма: {amount_user} {currency_user}"
            )

    print("Распечатываю итоговый список транзакций...")
    print()
    if len(data) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(data)}")
        for transaction in data:
            print()
            print(formatted_response(transaction))


if __name__ == "__main__":
    main()
