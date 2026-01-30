import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
LOG_FILE = "app.log"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

log_path = os.path.join(LOG_DIR, LOG_FILE)

def get_logger(name="automation_suite"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = RotatingFileHandler(
            log_path,
            maxBytes=5_000_000,   # 5 MB
            backupCount=5
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

