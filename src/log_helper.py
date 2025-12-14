import logging
import os


def create_file_handler(filename: str = "app.log") -> logging.FileHandler:
    """Возвращает FileHandler с правильным путём к логам"""
    log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", filename)  # поднимаемся в корень
    return logging.FileHandler(log_path, mode="w", encoding="utf-8")
