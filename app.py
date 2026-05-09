import streamlit as st
from moviepy.editor import *
import tempfile

st.title("Creator Studio Pro")

tool = st.sidebar.selectbox(
    "Select Tool",
    [
        "Logo Watermark",
        "Text Watermark"
    ]
)

video = st.file_uploader("Upload Video", type=["mp4"])

if video:

    temp_video = tempfile.NamedTemporaryFile(delete=False)
    temp_video.write(video.read())

    video_path = temp_video.name

    # -------------------
    # LOGO WATERMARK
    # -------------------

    if tool == "Logo Watermark":

        logo = st.file_uploader("Upload Logo", type=["png"])

        if logo and st.button("Process"):

            temp_logo = tempfile.NamedTemporaryFile(delete=False)
            temp_logo.write(logo.read())

            logo_path = temp_logo.name

            clip = VideoFileClip(video_path)

            logo_clip = (
                ImageClip(logo_path)
                .set_duration(clip.duration)
                .resize(height=60)
                .set_pos(("right", "bottom"))
                .set_opacity(0.5)
            )

            final = CompositeVideoClip([clip, logo_clip])

            output = "logo_output.mp4"

            final.write_videofile(output)

            st.success("Completed")
            st.video(output)

    # -------------------
    # TEXT WATERMARK
    # -------------------

    elif tool == "Text Watermark":

        text = st.text_input("Enter Text")

        if st.button("Process"):

            clip = VideoFileClip(video_path)

            txt = (
                TextClip(
                    text,
                    fontsize=40,
                    color="white"
                )
                .set_duration(clip.duration)
                .set_pos("center")
            )

            final = CompositeVideoClip([clip, txt])

            output = "text_output.mp4"

            final.write_videofile(output)

            st.success("Completed")
            st.video(output)
