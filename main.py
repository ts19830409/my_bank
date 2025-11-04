from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    print(get_mask_card_number("1234567890123456"))
    print(get_mask_account("12345678901234567890"))