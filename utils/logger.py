import logging
import os
from datetime import datetime

# Создаём директорию logs/, если её нет
LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

# Имя файла лога с текущей датой
log_file = os.path.join(LOG_DIR, f'test_log_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log')

# Настройка логгера
logger = logging.getLogger("ui_test_logger")
logger.setLevel(logging.DEBUG)  # Можно установить INFO, если не нужно слишком много деталей

# Обработчик для записи в файл
file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Обработчик для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Формат логов
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавляем обработчики, если ещё не добавлены
if not logger.hasHandlers():
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
