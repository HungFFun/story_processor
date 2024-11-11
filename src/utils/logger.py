from loguru import logger
import sys
from pathlib import Path
from datetime import datetime
from config import Config

def setup_logger():
    """Khởi tạo và cấu hình logger"""
    # Xóa handler mặc định
    logger.remove()

    # Thêm handler cho console
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=Config.LOG_LEVEL
    )

    # Thêm handler cho file
    log_file = Config.LOGS_DIR / f"app_{datetime.now().strftime('%Y%m%d')}.log"
    logger.add(
        log_file,
        format=Config.LOG_FORMAT,
        rotation="500 MB",
        retention="10 days",
        compression="zip",
        level=Config.LOG_LEVEL
    )
    
    return logger

# Khởi tạo logger
logger = setup_logger()