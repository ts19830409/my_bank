import csv
from unittest.mock import Mock, patch

from src.transactions import load_csv_file, load_xlsx_file


# ================== ТЕСТЫ ДЛЯ CSV ==================
def test_csv_normal():
    """Проверяем обычную работу CSV"""
    with patch("os.path.exists") as mock_exists:
        with patch("os.path.getsize") as mock_size:
            mock_exists.return_value = True
            mock_size.return_value = 100

            # Замокаем открытие файла и DictReader
            fake_file = Mock()
            fake_file.__enter__ = Mock(return_value=fake_file)
            fake_file.__exit__ = Mock(return_value=None)

            fake_reader = Mock()
            fake_reader.__iter__ = Mock(
                return_value=iter([{"id": "123", "amount": "500"}, {"id": "456", "amount": "1000"}])
            )

            with patch("builtins.open", return_value=fake_file):
                with patch("csv.DictReader", return_value=fake_reader):
                    result = load_csv_file("any.csv")

                    assert len(result) == 2
                    assert result[0]["id"] == "123"


def test_csv_no_file():
    """Проверяем, если файла нет"""
    with patch("os.path.exists", return_value=False):
        result = load_csv_file("missing.csv")
        assert result == []


def test_csv_empty():
    """Проверяем пустой файл"""
    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=0):
            result = load_csv_file("empty.csv")
            assert result == []


def test_csv_general_exception():
    """Любая другая ошибка при чтении CSV"""
    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=100):
            with patch("builtins.open", side_effect=PermissionError("Нет доступа")):
                result = load_csv_file("test.csv")
                assert result == []


def test_csv_minimal_error_test():
    """Минимальный тест для покрытия except csv.Error"""

    # Создаем callable, который вызывает csv.Error
    class ErrorRaiser:
        def __init__(self, *args, **kwargs):
            raise csv.Error("CSV parsing failed")

    with patch("csv.DictReader", ErrorRaiser):
        with patch("os.path.exists", return_value=True):
            with patch("os.path.getsize", return_value=100):
                with patch("builtins.open", Mock()):
                    result = load_csv_file("test.csv")
                    # Просто проверяем что не упало и вернуло список
                    assert isinstance(result, list)


def test_csv_empty_after_exists_check():
    """Проверяем случай, когда файл существует, но пустой"""
    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=0):
            result = load_csv_file("empty.csv")
            assert result == []


# ================== ТЕСТЫ ДЛЯ EXCEL ==================
def test_excel_normal():
    """Проверяем обычную работу Excel"""
    with patch("os.path.exists") as mock_exists:
        with patch("os.path.getsize") as mock_size:
            mock_exists.return_value = True
            mock_size.return_value = 100

            # Создаем фейковый DataFrame
            fake_df = Mock()
            fake_df.to_dict.return_value = [{"id": 777, "sum": 5000}, {"id": 888, "sum": 7000}]

            with patch("pandas.read_excel", return_value=fake_df):
                result = load_xlsx_file("any.xlsx")

                assert len(result) == 2
                assert result[0]["id"] == 777


def test_excel_error():
    """Проверяем ошибку при чтении Excel"""
    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=100):
            # Симулируем ошибку
            with patch("pandas.read_excel", side_effect=Exception("Ошибка!")):
                result = load_xlsx_file("broken.xlsx")
                assert result == []


def test_excel_no_file():
    """Проверяем, если Excel файла нет"""
    with patch("os.path.exists", return_value=False):
        result = load_xlsx_file("missing.xlsx")
        assert result == []


def test_excel_general_exception():
    """Любая ошибка при чтении Excel"""
    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=100):
            with patch("pandas.read_excel", side_effect=OSError("Диск недоступен")):
                result = load_xlsx_file("test.xlsx")
                assert result == []


def test_excel_empty_file():
    """Проверяем пустой Excel файл"""
    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=0):
            result = load_xlsx_file("empty.xlsx")
            assert result == []


def test_excel_file_exists_but_empty():
    """Альтернативный тест на пустой файл (для полного покрытия)"""
    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=0):
            result = load_xlsx_file("empty.xlsx")
            assert result == []
