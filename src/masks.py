def get_mask_card_number(card_num: str) -> str:
    """Маскирует номер банковской карты"""
    mask_card = str(card_num)
    if len(mask_card) == 16:
        return f"{mask_card[:4]} {mask_card[4:6]}** **** {mask_card[-4:]}"
    else:
        return "Не верно введен номер карты"


def get_mask_account(account: str) -> str:
    """Маскирует номер счета"""
    mask_account = str(account)
    if len(mask_account) == 20:
        return f"**{mask_account[-4:]}"
    else:
        return "Не верно введен номер счета"
