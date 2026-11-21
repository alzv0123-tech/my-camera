import streamlit as st

st.set_page_config(page_title="دوربین آنلاین", layout="wide")
st.title("پنل نظارت بر دوربین کاربران")

# تعریف تنظیمات اتصال امن
rtc_configuration = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]}
    ]
}

try:
    # فراخوانی مستقیم تابع بدون نیاز به کلاس WebRtcMode
    video = st.webrtc.streamer(
        key="camera-stream",
        mode="recv-send", # حالت استاندارد برای تماس دوطرفه
        rtc_configuration=rtc_configuration,
        media_stream_constraints={"video": True, "audio": False}
    )

    if hasattr(video, 'video_track') and video.video_track is not None:
        st.success("✅ تصویر کاربر دریافت شد.")
    else:
        st.info("⏳ منتظر اتصال کاربر...")

except Exception as e:
    st.error(f"خطا: {e}")
