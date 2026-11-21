import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

# تنظیمات ظاهری
st.set_page_config(page_title="دوربین آنلاین", layout="wide")
st.title("📹 پنل نظارت بر دوربین کاربران")

# درخواست دسترسی به دوربین کاربر
try:
    # WebRtcMode.SEND_ONLY یعنی فقط تصویر کاربر ارسال شود
    # اگر می‌خواهید صدای خودتان را هم بشنوید، حالت را به RECV_SEND تغییر دهید
    video = webrtc_streamer(
        key="camera-stream",
        mode=WebRtcMode.SEND_ONLY,
        rtc_configuration={
            "iceServers": [
                {"urls": ["stun:stun.l.google.com:19302"]}
            ]
        },
        media_stream_constraints={"video": True, "audio": False}
    )
    
    if video.video_track:
        st.success("✅ تصویر کاربر دریافت شد.")
    else:
        st.info("⏳ منتظر اتصال کاربر...")

except Exception as e:
    st.error(f"خطا در ارتباط: {e}")