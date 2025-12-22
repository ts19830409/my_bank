import logging

from src.log_helper import create_file_handler

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = create_file_handler("masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_num: str) -> str:
    """Маскирует номер банковской карты"""
    mask_card = str(card_num)
    logger.debug(f"Получили номер карты {mask_card}")
    if len(mask_card) == 16 and mask_card.isdigit():
        mask_card_formatted = f"{mask_card[:4]} {mask_card[4:6]}** **** {mask_card[-4:]}"
        logger.info(f"Номер карты {mask_card} успешно замаскирован: {mask_card_formatted}")
        return mask_card_formatted
    else:
        logger.error(f"Номер карты {mask_card} должен состоять из 16 цифр")
        return "Не верно введен номер карты"


def get_mask_account(account: str) -> str:
    """Маскирует номер счета"""
    mask_account = str(account)
    logger.debug(f"Получили номер счета {mask_account}")
    if len(mask_account) == 20 and mask_account.isdigit():
        mask_account_formatted = f"**{mask_account[-4:]}"
        logger.info(f" Номер счета {mask_account} успешно замаскирован: {mask_account_formatted}")
        return mask_account_formatted
    else:
        logger.error(f"Номер счета {mask_account} должен состоять из 20 цифр")
        return "Не верно введен номер счета"
