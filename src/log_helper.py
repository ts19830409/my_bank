import logging
import os


def create_file_handler(filename: str = "app.log") -> logging.FileHandler:
    """Возвращает FileHandler с правильным путём к логам"""
    log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", filename)  # поднимаемся в корень
    log_dir = os.path.dirname(log_path)
    os.makedirs(log_dir, exist_ok=True)
    return logging.FileHandler(log_path, mode="w", encoding="utf-8")
