from time import time


def log(filename=None):
    """Декоратор для автоматически логирования работы функции"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time()
            start_msg = f"{func.__name__} started at {start_time}"

            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(start_msg + "\n")
            else:
                print(start_msg)

            try:
                result = func(*args, **kwargs)

                finish_time = time()
                finish_msg = f"{func.__name__} finished with result: {result} at {finish_time}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(finish_msg + "\n")
                else:
                    print(finish_msg)

                return result

            except Exception as e:
                error_time = time()
                error_msg = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs} at {error_time}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_msg + "\n")
                else:
                    print(error_msg)

                raise

        return wrapper

    return decorator
