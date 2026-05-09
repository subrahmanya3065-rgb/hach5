from moviepy.editor import *
import cv2
import numpy as np
import noisereduce as nr
import os

def add_logo_fullscreen(video_path, logo_path, output, opacity=0.2):
    video = VideoFileClip(video_path).set_opacity(0.8) # 80% intensity for main video
    logo = (ImageClip(logo_path)
            .set_duration(video.duration)
            .resize((video.w, video.h))
            .set_position("center")
            .set_opacity(opacity)) # 20% intensity (0.2)
    
    final = CompositeVideoClip([video, logo])
    # Compression: bitrate="2000k" reduces file size
    final.write_videofile(output, codec="libx264", audio_codec="aac", bitrate="2000k")

def process_audio_and_ads(video_path, ad_path=None, custom_audio_path=None, reduce_noise=False, output_path="outputs/final_pro.mp4"):
    video = VideoFileClip(video_path)
    
    # 1. Noise Reduction
    if reduce_noise and video.audio is not None:
        sr = video.audio.fps
        audio_array = video.audio.to_soundarray(fps=sr)
        # Apply noise reduction on the sound array
        reduced_audio_array = nr.reduce_noise(y=audio_array.T, sr=sr).T
        video.audio = AudioArrayClip(reduced_audio_array, fps=sr)

    # 2. Custom Background Music
    if custom_audio_path:
        bg_music = AudioFileClip(custom_audio_path).set_duration(video.duration)
        video = video.set_audio(bg_music)
