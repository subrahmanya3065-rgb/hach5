from moviepy.editor import *
import cv2
import numpy as np

# =====================================
# FULL SCREEN LOGO WATERMARK
# =====================================

def add_logo_fullscreen(video_path, logo_path, output, opacity=0.2):

    # LOAD MAIN VIDEO
    video = VideoFileClip(video_path)

    # LOAD LOGO
    logo = (
        ImageClip(logo_path)
        .set_duration(video.duration)

        # FULL SCREEN SIZE
        .resize((video.w, video.h))

        # CENTER POSITION
        .set_position(("center", "center"))

        # TRANSPARENCY
        .set_opacity(opacity)
    )

    # COMBINE VIDEO + LOGO
    final = CompositeVideoClip([video, logo])

    # EXPORT VIDEO
    final.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
    )


# =====================================
# CUSTOM TEXT BRANDING
# =====================================

def add_text_branding(video_path, text, output):

    # TEMP FILE
    temp_output = "temp/temp_branding.mp4"

    # LOAD VIDEO
    cap = cv2.VideoCapture(video_path)

    # VIDEO SETTINGS
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # VIDEO WRITER
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(
        temp_output,
        fourcc,
        fps,
        (width, height)
    )

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # COPY FRAME
        overlay = frame.copy()

        # FONT SETTINGS
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 3
        thickness = 5

        # TEXT SIZE
        text_size = cv2.getTextSize(
            text,
            font,
            font_scale,
            thickness
        )[0]

        # CENTER POSITION
        x = (width - text_size[0]) // 2
        y = height // 2

        # DRAW TEXT
        cv2.putText(
            overlay,
            text,
            (x, y),
            font,
            font_scale,
            (255, 255, 255),
            thickness,
            cv2.LINE_AA
        )

        # TEXT TRANSPARENCY
        alpha = 0.5

        # BLEND TEXT + VIDEO
        frame = cv2.addWeighted(
            overlay,
            alpha,
            frame,
            1 - alpha,
            0
        )

        # WRITE FRAME
        out.write(frame)

    # RELEASE VIDEO
    cap.release()
    out.release()

    # RE-ENCODE FOR BROWSER PLAYBACK
    final_clip = VideoFileClip(temp_output)

    final_clip.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
    )
    # =====================================
# ADD INTRO VIDEO
# =====================================
# =====================================
# ADD INTRO VIDEO
# =====================================

def add_intro_video(intro_path, main_video_path, output):

    # LOAD VIDEOS
    intro = VideoFileClip(intro_path)
    main_video = VideoFileClip(main_video_path)

    # MATCH RESOLUTION
    intro = intro.resize(main_video.size)

    # MATCH FPS
    intro = intro.set_fps(main_video.fps)

    # COMBINE VIDEOS
    final_video = concatenate_videoclips(
        [intro, main_video],
        method="compose"
    )

    # EXPORT FINAL VIDEO
    final_video.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac",
        fps=main_video.fps
    )
