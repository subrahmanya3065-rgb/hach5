import streamlit as st
import os

from branding_tools import *

# CREATE FOLDERS
os.makedirs("temp", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# PAGE SETTINGS
st.set_page_config(
    page_title="Creator Studio Pro",
    layout="wide"
)

# TITLE
st.title("🎬 Creator Studio Pro")

# SIDEBAR MENU
menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Full Screen Watermark",
        "Custom Text Branding",
        "Add Intro Video"
    ]
)

# =========================================
# FULL SCREEN WATERMARK
# =========================================

if menu == "Full Screen Watermark":

    st.header("🖼️ Full Screen Watermark")

    video = st.file_uploader(
        "Upload Video",
        type=["mp4"]
    )

    logo = st.file_uploader(
        "Upload PNG Logo",
        type=["png"]
    )

    if video and logo:

        # SAVE VIDEO
        with open("temp/input.mp4", "wb") as f:
            f.write(video.read())

        # SAVE LOGO
        with open("temp/logo.png", "wb") as f:
            f.write(logo.read())

        if st.button("Apply Watermark"):

            add_logo_fullscreen(
                "temp/input.mp4",
                "temp/logo.png",
                "outputs/logo_output.mp4",
                opacity=0.2
            )

            st.success("Watermark Added Successfully!")

            st.video("outputs/logo_output.mp4")

            with open("outputs/logo_output.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="watermarked_video.mp4"
                )

# =========================================
# CUSTOM TEXT BRANDING
# =========================================

if menu == "Custom Text Branding":

    st.header("📝 Custom Text Branding")

    text_video = st.file_uploader(
        "Upload Video",
        type=["mp4"]
    )

    branding_text = st.text_input(
        "Enter Your Branding Text"
    )

    if text_video and branding_text:

        with open("temp/text_video.mp4", "wb") as f:
            f.write(text_video.read())

        if st.button("Apply Text Branding"):

            add_text_branding(
                "temp/text_video.mp4",
                branding_text,
                "outputs/text_branding.mp4"
            )

            st.success("Text Branding Added Successfully!")

            st.video("outputs/text_branding.mp4")

            with open("outputs/text_branding.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="text_branding_video.mp4"
                )

# =========================================
# ADD INTRO VIDEO
# =========================================

if menu == "Add Intro Video":

    st.header("🎬 Add Intro Video")

    intro_video = st.file_uploader(
        "Upload Intro Clip",
        type=["mp4"]
    )

    main_video = st.file_uploader(
        "Upload Main Video",
        type=["mp4"]
    )

    if intro_video and main_video:

        # SAVE INTRO
        with open("temp/intro.mp4", "wb") as f:
            f.write(intro_video.read())

        # SAVE MAIN VIDEO
        with open("temp/main_video.mp4", "wb") as f:
            f.write(main_video.read())

        if st.button("Generate Final Video"):

            add_intro_video(
                "temp/intro.mp4",
                "temp/main_video.mp4",
                "outputs/final_intro_video.mp4"
            )

            st.success("Intro Added Successfully!")

            st.video("outputs/final_intro_video.mp4")

            with open("outputs/final_intro_video.mp4", "rb") as file:

                st.download_button(
                    "Download Video",
                    file,
                    file_name="final_intro_video.mp4"
                )
