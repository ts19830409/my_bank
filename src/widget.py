from src.masks import get_mask_card_number, get_mask_account
def mask_account_card(full_string: str) -> str:
    full_name = full_string.split()
    number = full_name[-1]
    if len(number) == 16:
        name = " ".join (full_name[:-1])
        number = get_mask_card_number(number)
        return f"{name} {number}"
    elif len(number) == 20:
        name = " ".join (full_name[:-1])
        number = get_mask_account(number)
        return f"{name} {number}"
    else:
        return "Введены не корректные значения"



