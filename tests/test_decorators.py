import os
import tempfile

from src.decorators import log


def test_log_console_success(capsys):
    """Тест логирования УСПЕШНОГО выполнения функции в консоль"""

    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "add ok" in captured.out


def test_log_console_error(capsys):
    """Тест логирования ОШИБКИ выполнения функции в консоль"""

    @log()
    def error_func():
        raise ValueError("Это тестовая ошибка")

    try:
        error_func()
    except ValueError:
        pass
    captured = capsys.readouterr()
    assert "error_func error: ValueError" in captured.out
    assert "Inputs: (), {}" in captured.out


def test_log_file_success():
    """Тест логирования УСПЕШНОГО выполнения функции в файл"""

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".log") as tmp:
        tmp_filename = tmp.name

    try:

        @log(filename=tmp_filename)
        def multiply(x, y):
            return x * y

        result = multiply(3, 4)

        with open(tmp_filename, "r") as f:
            content = f.read()

        assert result == 12
        assert "multiply ok" in content

    finally:
        os.unlink(tmp_filename)


def test_log_file_error():
    """Тест логирования ОШИБКИ выполнения функции в файл"""

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".log") as tmp:
        tmp_filename = tmp.name

    try:

        @log(filename=tmp_filename)  # ← в файл!
        def failing():
            raise TypeError("file test error")

        try:
            failing()
        except TypeError:
            pass

        with open(tmp_filename, "r") as f:
            content = f.read()

        assert "failing error: TypeError" in content
        assert "Inputs: (), {}" in content

    finally:
        os.unlink(tmp_filename)
