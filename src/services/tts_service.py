from pathlib import Path
from typing import List
import openai
from config import Config
from utils.logger import logger
import os

class TTSService:
    """Service xử lý text-to-speech sử dụng OpenAI API"""
    
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.model = Config.TTS_MODEL
        self.voice = Config.TTS_VOICE
    
    def generate_audio(self, text_files: List[Path], output_dir: Path) -> List[Path]:
        """
        Tạo file audio từ các file văn bản
        Args:
            text_files: Danh sách các file văn bản
            output_dir: Thư mục đầu ra
        Returns:
            List[Path]: Danh sách các file audio
        """
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            audio_files = []
            
            for i, text_file in enumerate(text_files, 1):
                text = text_file.read_text(encoding='utf-8')
                output_path = output_dir / f'part{i:03d}.mp3'
                
                response = openai.audio.speech.create(
                    model=self.model,
                    voice=self.voice,
                    input=text
                )
                
                # Lưu audio
                response.stream_to_file(str(output_path))
                audio_files.append(output_path)
                
                logger.info(f"Đã tạo audio {i}/{len(text_files)}")
            
            return audio_files
            
        except Exception as e:
            logger.error(f"Lỗi khi tạo audio: {str(e)}")
            raise