import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.set_page_config(page_title="دوربین آنلاین", layout="wide")
st.title("📹 پنل نظارت بر دوربین کاربران")

try:
    # بدون نیاز به تعریف دستی WebRtcMode
    video = webrtc_streamer(
        key="camera-stream",
        mode="recv-send",
        media_stream_constraints={"video": True, "audio": False}
    )

    if video.video_track:
        st.success("✅ تصویر کاربر دریافت شد.")
    else:
        st.info("⏳ منتظر اتصال کاربر...")

except Exception as e:
    st.error(f"خطا: {e}")
