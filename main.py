#from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


def main ( ) :
    print ( "=== Тестирование маскировки банковских данных ===" )

    tests = [
        "Maestro 1596837868705199" ,
        "Счет 64686473678894779589" ,
        "MasterCard 7158300734726758" ,
        "Счет 35383033474447895560" ,
        "Visa Classic 6831982476737658" ,
        "Visa Platinum 8990922113665229" ,
        "Visa Gold 5999414228426353" ,
        "Счет 73654108430135874305"
    ]

    for test in tests :
        result = mask_account_card(test)
        print (f"Ввод: {test}")
        print (f"Вывод: {result}")
        print ()

    print("=== Тестирование форматирования даты ===")
    test_data = "2024-03-11T02:26:18.671407"
    result_data = get_date(test_data)
    print(f"Ввод:  {test_data}")
    print(f"Вывод: {result_data}")


if __name__ == "__main__":
    main()

    #print(get_mask_card_number("1234567890123456"))
    #print(get_mask_account("12345678901234567890"))


