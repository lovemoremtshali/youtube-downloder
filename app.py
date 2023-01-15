import streamlit as st
import time
import downloder
def main():
    title, mid, logo = st.columns([40,1,40])
    with title:
        st.title("Youtube")
        st.title("Downloader")
    with logo:
        st.image("logo.png")
    
    txt_input, btn = st.columns([10,1])
    
    txt =st.text_input("Enter URL")
    if 'state' not in st.session_state:
        st.session_state['state']=False
    if (st.button("Process link",on_click=callback) or st.session_state.state):
        if txt== '':
            st.warning('enter a url')
        else:
            with st.spinner("Processing..."):
                try:
                    url = downloder.Get_res(txt)
                    d_vid, pic = st.columns([1,4])
                    with d_vid:
                        if url.r_144p()==None:
                            st.button(label="144p not available", disabled=True)
                        else:
                            if st.button(label="144p res"):
                                url.r_144p().download()

                        if url.r_360p()==None:
                            st.button(label="360p not available", disabled=True)
                        else:
                            st.button(label="360p res")

                        if url.r_720p()==None:
                            st.button(label="720p not available", disabled=True)
                        else:
                            st.button(label="720p res")
                    with pic:
                        st.image(url.thumb_nail())

                except:
                    st.warning("Enter a valid URL")
                
        st.success("Done")


def callback():
    st.session_state.state = True



if __name__ == '__main__':
    main()