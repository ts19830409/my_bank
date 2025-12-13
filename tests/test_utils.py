import os
import tempfile

from src.utils import load_json_file


def test_load_good_json():
    """Тест на загрузку файла"""
    # Создаем файл вручную
    with open("test_file.json", "w", encoding="utf-8") as f:
        f.write('[{"test": 1}]')

    result = load_json_file("test_file.json")
    assert result == [{"test": 1}]
    os.remove("test_file.json")


def test_load_missing_file():
    """Тест на отсутствие файла"""
    result = load_json_file("non_existent_file.json")
    assert result == []


def test_load_invalid_json():
    """Тест на корректность JSON синтаксис"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        f.write("{invalid json}")
        file_path = f.name

    try:
        result = load_json_file(file_path)
        assert result == []
    finally:
        os.unlink(file_path)


def test_load_json_not_list():
    """Тест на корректность JSON файла"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        f.write('{"key": "value"}')
        file_path = f.name

    try:
        result = load_json_file(file_path)
        assert result == []
    finally:
        os.unlink(file_path)


def test_load_json_empty_list():
    """Тест на пустой список"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        f.write("[]")
        file_path = f.name

    try:
        result = load_json_file(file_path)
        assert result == []
    finally:
        os.unlink(file_path)
