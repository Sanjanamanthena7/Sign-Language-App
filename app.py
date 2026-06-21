import av
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import mediapipe as mp

# ✅ Make sure backend is a package (has __init__.py)
from backend.camera_stream import process_frame

st.set_page_config(
    page_title=":rainbow[Sign Language Detection]",
    page_icon="🤟",
    layout="wide"
)

st.title("🤟 Sign Language Detection")

col1, col2 = st.columns([3, 1])

with col2:
    st.info("""
### Supported Signs

✊ FIST  
✋ FIVE  
☝ ONE  
✌ VICTORY  
👍 THUMBS UP  
🤟 LOVE YOU  
L
""")

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = process_frame(img)   # ✅ Calls your backend function
        return av.VideoFrame.from_ndarray(img, format="bgr24")

with col1:
    webrtc_streamer(
        key="gesture",
        video_processor_factory=VideoProcessor,
        media_stream_constraints={
            "video": True,
            "audio": False
        }
    )
