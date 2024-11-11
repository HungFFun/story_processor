from pathlib import Path
from typing import List
from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, concatenate_videoclips
from config import Config
from utils.logger import logger

class VideoProcessor:
    """Service xử lý và tạo video"""
    
    def __init__(self):
        self.config = Config.VIDEO_CONFIG
        self.background_path = Config.ASSETS_DIR / 'background.jpg'
        
    def create_segment_video(self, audio_file: Path, output_dir: Path, part_num: int) -> Path:
        """
        Tạo video cho một đoạn audio
        Args:
            audio_file: File audio
            output_dir: Thư mục đầu ra
            part_num: Số thứ tự đoạn
        Returns:
            Path: Đường dẫn file video
        """
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / f'part{part_num:03d}.mp4'
            
            # Tạo video từ ảnh nền và audio
            audio = AudioFileClip(str(audio_file))
            image = ImageClip(str(self.background_path))
            
            video = image.set_duration(audio.duration)
            video = video.set_audio(audio)
            
            video.write_videofile(
                str(output_path),
                fps=self.config['fps'],
                codec=self.config['video_codec'],
                audio_codec=self.config['audio_codec'],
                audio_bitrate=self.config['audio_bitrate']
            )
            
            # Đóng clips
            video.close()
            audio.close()
            
            return output_path
            
        except Exception as e:
            logger.error(f"Lỗi khi tạo video segment: {str(e)}")
            raise
    
    def merge_videos(self, video_files: List[Path], output_path: Path) -> Path:
        """
        Ghép các video segments thành video hoàn chỉnh
        Args:
            video_files: Danh sách các file video
            output_path: Đường dẫn file đầu ra
        Returns:
            Path: Đường dẫn video hoàn chỉnh
        """
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Đọc các video segments
            clips = [VideoFileClip(str(file)) for file in video_files]
            
            # Ghép các clips
            final_video = concatenate_videoclips(clips)
            
            # Xuất video hoàn chỉnh
            final_video.write_videofile(
                str(output_path),
                fps=self.config['fps'],
                codec=self.config['video_codec'],
                audio_codec=self.config['audio_codec'],
                audio_bitrate=self.config['audio_bitrate']
            )
            
            # Đóng clips
            for clip in clips:
                clip.close()
            final_video.close()
            
            return output_path
            
        except Exception as e:
            logger.error(f"Lỗi khi ghép video: {str(e)}")
            raise