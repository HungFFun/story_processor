from .logger import logger, setup_logger
from .file_helper import FileHelper
from .validation import ValidationHelper
from .performance import PerformanceMonitor
from contextlib import contextmanager
import time

__all__ = [
    'logger',
    'setup_logger',
    'FileHelper',
    'ValidationHelper',
    'PerformanceMonitor'
]

@contextmanager
def measure_time(name: str):
    """Context manager để đo thời gian thực thi"""
    start_time = time.time()
    yield
    duration = time.time() - start_time
    logger.info(f"{name} took {duration:.2f} seconds")