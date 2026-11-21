import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.set_page_config(page_title="دوربین آنلاین", layout="wide")
st.title("📹 پنل نظارت بر دوربین کاربران")

# تعریف سرور STUN برای عبور از فایروال‌ها
rtc_configuration = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]}
    ]
}

try:
    # استفاده از حالت RECV_SEND برای اطمینان از اتصال دوطرفه
    # اگر فقط تصویر کاربر را می‌خواهید، این بهترین حالت است
    video = webrtc_streamer(
        key="camera-stream",
        mode=WebRtcMode.RECV_SEND, 
        rtc_configuration=rtc_configuration,
        media_stream_constraints={"video": True, "audio": False}
    )

    if video.video_track:
        st.success("✅ تصویر کاربر دریافت شد.")
    else:
        st.info("⏳ منتظر اتصال کاربر...")

except Exception as e:
    st.error(f"خطا در ارتباط: {e}")
