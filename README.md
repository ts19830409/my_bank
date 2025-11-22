# Виджет операций для личного кабинета банка

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
```

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
