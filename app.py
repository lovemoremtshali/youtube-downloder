import streamlit as st
import time
def main():
    title, mid, logo = st.columns([40,1,40])
    with title:
        st.title("Youtube")
        st.title("Downloader")
    with logo:
        st.image("logo.png")
    
    txt_input, btn = st.columns([10,1])
    
    st.text_input("Enter URL")
    
    if st.button("Process link"):
        with st.spinner("Processing..."):
            time.sleep(5)
        st.success("Done")






if __name__ == '__main__':
    main()