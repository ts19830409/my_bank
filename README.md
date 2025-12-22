﻿# Виджет операций для личного кабинета банка

## Описание
Виджет для отображения последних успешных банковских операций клиента в личном кабинете банка. 
Проект предоставляет функционал для безопасного отображения номеров карт и счетов с использованием масок.

## Функционал проекта.

## Пакет src

### Модуль masks
Содержит функции для наложения масок на конфиденциальные данные:

**get_mask_card_number(card_number: str) -> str**

Маскирует номер банковской карты в формате: XXXX XX** **** XXXX
Пример: 7000792289606361 → 7000 79** **** 6361

**get_mask_account(account_number: str) -> str**

Маскирует номер счета в формате: **XXXX
**Пример:** 73654108430135874305 → **4305

### Модуль widget
Содержит функции для работы с банковскими данными:

**mask_account_card(card_or_account_data: str) -> str**

Автоматически определяет тип данных (карта или счет) и применяет соответствующую маску.
**Пример для карты:** Visa Platinum 7000792289606361 → Visa Platinum 7000 79** **** 6361
**Пример для счета:** Счет 73654108430135874305 → Счет **4305

**get_date(data_info: str) -> str**
Функция берёт данные даты и времени в формате "2024-03-11T02:26:18.671407"
и возвращает только дату в формате 'ДД.ММ.ГГГГ'"""

### Модуль processing
 Модуль processing предоставляет функции для фильтрации и сортировки банковских операций.

**filter_by_state(operations: list, state: str = 'EXECUTED') -> list**
Фильтрует список операций по статусу выполнения.

**Параметры:**

operations: Список словарей с операциями
state: Статус для фильтрации. По умолчанию 'EXECUTED'

**Пример использования:**
```
from processing import filter_by_state

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
    ]

# Фильтрация по статусу 'EXECUTED' (по умолчанию)
executed_operations = filter_by_state(operations)
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

# Фильтрация по статусу 'CANCELED'
canceled_operations = filter_by_state(operations, 'CANCELED')
# [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]
```
**sort_by_date(operations: list, reverse: bool = True) -> list**
Сортирует список операций по дате.

**Параметры:**

operations: Список словарей с операциями
reverse: Порядок сортировки(True (по умолчанию) - по убыванию, False - по возрастанию(сначала самые старые))

Пример использования:
```
operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]

# Сортировка по убыванию (сначала новые)
sorted_desc = sort_by_date(operations)
# [{'id': 41428829, ...}, {'id': 939719570, ...}]

# Сортировка по возрастанию (сначала старые)
sorted_asc = sort_by_date(operations, reverse=False)
# [{'id': 939719570, ...}, {'id': 41428829, ...}]
```
### Модуль generators
Содержит функции для работы с массивами транзакций:

**filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:**

Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
```
{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```

**transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:**

Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
```
    Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```
**card_number_generator(start: int, end: int) -> Iterator[str]:**

Генератор генерирует номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
```
    0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```
### Модуль generators
Создан декоратор log для автоматической регистрации выполнения функций.
**def log(filename=None):**
```
def log(filename=None):
    """Декоратор для автоматически логирования работы функции"""

    def decorator(func):
        def wrapper(*args, **kwargs):
        ...
```
### Модуль utils
Содержит функцию принимающая на вход JSON-файл и возвращающая список словарей
с данными о финансовых транзакциях
**def load_json_file**
```
	...
		with open(file_path, "r", encoding="utf-8") as f:
			parsed_data = json.load(f)
			if not isinstance(parsed_data, list):
				return[]
	...			
```
### Модуль external_api
Содержит функция, принимающая на вход транзакцию и возвращающая сумму транзакции
**def convert_to_rub**
```
    ...
        amount_user = transaction["operationAmount"]["amount"]
	    currency_user = transaction["operationAmount"]["currency"]["code"]
	    amount_user_convert = float(amount_user)
    ...	
```
### Модуль processing
Содержит функции принимающие на вход csv-файл и xlsx-файл и возвращающие список словарей
с данными о финансовых транзакциях
**def load_csv_file**
```
	...
        with open(file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=";")
            for row in reader:
               transactions.append(row)
            return transactions	
    ...			
```
**def load_xlsx_filee**
```
	...
		df = pd.read_excel(file_path)
        result = df.to_dict("records")
        return result
    ...
```
## Модуль search
Содержит функцию для поиска в списке словарей операций по заданной строке и 
функцию для подсчета количества банковских операций определенного типа
**def process_bank_search**
```
	result_search = []
	if search == "":
		return data
	else:
		pattern = re.compile(search, re.I)
		for transaction in data:
			description = transaction.get("description", "")
			if pattern.search(description):
				result_search.append(transaction)
	return result_search
```
**process_bank_operations**
```counter = Counter()
	for transaction in data:
		description = transaction.get("description", "")
		for category in categories:
			if re.search(category, description, re.I):
				counter[category] += 1
	return counter
```
## Пакет tests.

### Модуль test_masks
Содержит тестовые функции для проверки корректности работы функции get_mask_card_number 
и get_mask_account.

Тестовые функции написаны с использованием параметризации:
```
@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("700079228960636126", "Не верно введен номер карты"),
       ...
    ],
)
def test_get_mask_card_number(value, expected):
    ...


@pytest.mark.parametrize(
    "value, expected",
    [
        ("73654108430135874305", "**4305"),
        ("73654108430135874", "Не верно введен номер счета"),
       ...
    ],
)
def test_get_mask_account(value, expected):
    ...
```
### Модуль test_widget
Содержит тестовые функции для проверки корректности работы функции mask_account_card 
и get_date.

Тестовые функции написаны с использованием параметризации:
```
@pytest.mark.parametrize(
    "number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
      ...
    ],
)
def test_mask_account_card_valid(number, expected):
    ...


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Счет 646864736788947795 89", "Введены не корректные значения"),
        ("Счет 64686dfe473678894779589", "Введены не корректные значения"),
        ...
    ],
)
def test_mask_account_card_invalid(number, expected):
    ...


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("T02:26:18.671407", "Введена не корректная дата"),
        ...
    ],
)
def test_get_date(value, expected):
    ...
```
### Модуль test_processing
Содержит тестовые функции для проверки корректности работы функции filter_by_state 
и sort_by_date.

Тестовые функции написаны с использованием параметризации и фикстур:
```
@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
        ("PENDING", 0),
    ],
)
def test_filter_by_state(operations_data, state, expected_count):
    ...


def test_filter_by_state_default(operations_data):
    ...


def test_basic_functionality(sort_data):
    ...


def test_default_parameter(simple_data):
    ...


def test_empty_list():
    ...


def test_missing_date_key(invalid_data):
    ...
```
### Модуль test_generators
Содержит тестовые функции для проверки корректности работы функции filter_by_currency, 
transaction_descriptions и card_number_generator.

Тестовые функции написаны с использованием параметризации:
```
def test_filter_by_currency_correct(sample_transactions):
    ...


def test_filter_by_currency_no_matches(sample_transactions):
    ...


def test_filter_by_currency_empty_list():
   ...


def test_transaction_descriptions_multiple():
    ...


def test_transaction_descriptions_single():
    ...


def test_transaction_descriptions_empty():
    ...


@pytest.mark.parametrize(
    "start_num, end_num, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        )
    ],
)
def test_card_number_generator(start_num, end_num, expected):
    ...


@pytest.mark.parametrize(
    "start_num, end_num, expected",
    [
        (
            -5,
            -3,
            [
                "0000 0000 0000 0005",
                "0000 0000 0000 0004",
                "0000 0000 0000 0003",
            ],
        )
    ],
)
def test_card_number_generator_negative_values(start_num, end_num, expected):
    ...


@pytest.mark.parametrize("args", [(), (1,), (1, 2, 3)])
def test_card_number_generator_wrong_arguments(args):
    ...


def test_card_formatting():
    ...


@pytest.mark.parametrize(
    "start,end,expected_count",
    [
        (9999999999999990, 9999999999999999, 10),
        (0, 9, 10),
        (10000, 10000, 1),
    ],
)
def test_card_boundary_values(start, end, expected_count):
    ...


def test_generator_completion():
    ...
```
Фикстурыы описаны в пакете conftest:
```
@pytest.fixture
def operations_data():
    ...

@pytest.fixture
def sort_data():
    ...


@pytest.fixture
def simple_data():
    ...


@pytest.fixture
def invalid_data():
    ...


@pytest.fixture
def sample_transactions():
    ...
```
### Модуль test_decorators
Для тестирования была использована фикстура capsys
```
def test_log_console_success(capsys):
    """Тест логирования УСПЕШНОГО выполнения функции в консоль"""
    ...

def test_log_console_error(capsys):
    """Тест логирования ОШИБКИ выполнения функции в консоль"""

    ...


def test_log_file_success():
    """Тест логирования УСПЕШНОГО выполнения функции в файл"""

    ...


def test_log_file_error():
    """Тест логирования ОШИБКИ выполнения функции в файл"""

    ...

```
### Модуль test_utils
Содержит тестовые функции для проверки корректности работы функции load_json_file
```
def test_load_good_json():
    ...
    
def test_load_missing_file()
    ...

def test_load_invalid_json()
    ...
    
def test_load_json_not_list():
    ...

def test_load_json_empty_list():
    ...        
```
### Модуль test_external_api
Содержит тестовые функции для проверки корректности работы функции convert_to_rub 
с использованием Mock и patch
```
def test_rub_transaction():
    ...

def test_usd_transaction_with_mock():
    ...

def test_api_error():
    ...

def test_no_api_key():
    ...
```
### Модуль test_transactions
Содержит тестовые функции для проверки корректности работы функции load_csv_file и load_xlsx_file 
с использованием Mock и patch
```
def test_csv_normal:
    ...

def test_csv_no_file():
    ...

def test_csv_empty():
    ...

def test_csv_general_exception():
    ...

def test_csv_minimal_error_test():
    ...

def test_csv_empty_after_exists_check():
    ...
    
def test_excel_normal():
    ...

def test_excel_error():
    ...       
    
def test_excel_no_file():
    ...       
    
def test_excel_general_exception():
    ...

def test_excel_empty_file():
    ...
    
def test_excel_file_exists_but_empty():
    ...                   
```
### Модуль test_search
Содержит тестовые функции для проверки корректности работы функции process_bank_search и
process_bank_operations 
```
def test_process_bank_search_empty_data():
    ...

def test_process_bank_search_found():
    ...

def test_process_bank_search_not_found():
    ...

def test_process_bank_search_empty_search():
    ...

def test_process_bank_search_case_insensitive():
    ...

def test_process_bank_search_with_regex():
    ...
    
def test_process_bank_search_multiple_matches():
    ...

def test_process_bank_search_partial_match():
    ...       
    
def test_process_bank_operations_basic():
    ...       
    
def test_process_bank_operations_empty_data():
    ...

def test_process_bank_operations_no_matches():
    ...
    
def test_process_bank_operations_multiple_categories():
    ...                   

def test_process_bank_operations_case_insensitive():
    ...                   
    
def test_process_bank_operations_all_categories_zero():
    ...                   

def test_process_bank_search_missing_description():
    ...                   
   
def test_process_bank_operations_empty_categories():
    ...

def test_process_bank_search_special_characters():
    ...                   

def test_process_bank_search_performance():
    ...                   

def test_process_bank_operations_performance():
    ...
```
# Собран шаблон файла .env

# Модуле Main
Реализована функция отвечающая за основную логику проекта и связывающая
функциональности между собой

# Установка:
**Клонируйте репозиторий:**
```
git clone https://github.com/ts19830409/my_bank.git
```
# Разработка:

+ Проект находится в активной разработке. В ближайших планах:

+ Добавление новых модулей для расширения функционала

+ Улучшение обработки различных форматов данных

*Проект разработан в рамках учебного курса SkyPro*