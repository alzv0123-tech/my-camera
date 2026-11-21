import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

st.set_page_config(page_title="دوربین آنلاین", layout="wide")
st.title("📹 پنل نظارت بر دوربین کاربران")

# تعریف سرورهای STUN برای اتصال بهتر
rtc_configuration: RTCConfiguration = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]}
    ]
}

try:
    # تنظیمات دوربین کاربر
    # mode=WebRtcMode.RECV_SEND یعنی هم تصویر شما و هم تصویر کاربر قابل مشاهده باشد
    # اگر فقط می‌خواهید تصویر کاربر را ببینید (بدون صدا/تصویر خودتان)، 
    # می‌توانید از مد RECV_ONLY یا SEND_ONLY (با سینتکس جدید) استفاده کنید.
    
    video = webrtc_streamer(
        key="camera-stream",
        mode=WebRtcMode.SEND_ONLY, # این حالت فقط تصویر کاربر را ارسال می‌کند
        rtc_configuration=rtc_configuration,
        media_stream_constraints={"video": True, "audio": False}
    )

    if video.video_track:
        st.success("✅ تصویر کاربر دریافت شد.")
    else:
        st.info("⏳ منتظر اتصال کاربر...")

except Exception as e:
    st.error(f"خطا در ارتباط: {e}")
