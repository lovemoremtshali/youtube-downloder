import streamlit as st
import pytube
import requests
def main():


    st.title("YouTube Video Downloader")

    # Get YouTube video URL from user
    url = st.text_input("Enter YouTube video URL:")

    if url:
        try:
            # Create a YouTube object
            yt = pytube.YouTube(url)

            # Display available streams
            streams = yt.streams.filter(progressive=True)
            stream_option = st.selectbox("Select video quality:", streams)

            # Generate a download link when the button is clicked
            if st.button("Generate Download Link"):
                download_url = stream_option.url
                st.markdown(f'<a href="{download_url}" download="{yt.title}.mp4">Click here to download</a>', unsafe_allow_html=True)
                st.success("Download link generated. Click to save to your local device.")
        except Exception as e:
            st.error(f"Invalid URL or network error: {e}")




if __name__ == '__main__':
    main()