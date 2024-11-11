from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    """Cấu hình chung cho toàn bộ project"""
    
    # Đường dẫn thư mục
    PROJECT_DIR = Path(__file__).parent
    OUTPUT_DIR = PROJECT_DIR / os.getenv('OUTPUT_DIR', 'output')
    ASSETS_DIR = PROJECT_DIR / 'assets'
    LOGS_DIR = PROJECT_DIR / 'logs'
    
    # Cấu hình Google Docs
    CREDENTIALS_PATH = PROJECT_DIR / 'src' / 'config' / 'credentials.json'
    SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
    
    # Cấu hình TTS
    TTS_MODEL = "tts-1-hd"
    TTS_VOICE = "onyx"
    TTS_MAX_CHARS = 4000
    
    # Cấu hình Video
    VIDEO_CONFIG = {
        'width': 1920,
        'height': 1080,
        'fps': 24,
        'video_codec': 'libx264',
        'audio_codec': 'aac',
        'audio_bitrate': '192k'
    }
    
    # Cấu hình xử lý text
    TEXT_CONFIG = {
        'paragraph_separator': '\n\n',
        'sentence_separator': '(?<=[.!?]) +',
        'min_segment_length': 100,
        'max_segment_length': 4000
    }
    
    # Cấu hình logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FORMAT = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}"
    
    @classmethod
    def init_directories(cls):
        """Khởi tạo các thư mục cần thiết"""
        for directory in [cls.OUTPUT_DIR, cls.ASSETS_DIR, cls.LOGS_DIR]:
            directory.mkdir(parents=True, exist_ok=True)