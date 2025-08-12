from utils.logger import logger
from functools import wraps


def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Вызов: {func.__qualname__} с args={args[1:]}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Завершено: {func.__qualname__}")
        return result

    return wrapper
