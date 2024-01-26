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
    print("hey")
    txt =st.text_input("Enter URL")
    if 'state' not in st.session_state:
        st.session_state['state']=False
    if (st.button("Process link",on_click=callback) or st.session_state.state):
        if txt== '':
            st.warning('enter a url')
        else:
            with st.spinner("Processing..."):
                try:
                    print(1)
                    url = downloder.Get_res(txt)
                    print(1)
                    d_vid,aud, pic = st.columns([1,1,4])
                    print(1)
                    with d_vid:
                        st.write("### Videos")
                        if url.r_144p()==None:
                            st.button(label="144p not available", disabled=True)
                        else:
                            if st.button(label="144p res"):
                                url.r_144p().download()
                                #st.experimental_rerun()

                        if url.r_360p()==None:
                            st.button(label="360p not available", disabled=True)
                        else:
                            if st.button(label="360p res"):
                                url.r_360p().download()

                        if url.r_720p()==None:
                            st.button(label="720p not available", disabled=True)
                        else:
                            if st.button(label="720p res"):
                                url.r_720p().download()
                    with aud:
                        st.write("### Audio")
                        if url.a_50()==None:
                            st.button(label="50kbps not available", disabled=True)
                        else:
                            if st.button(label="50kbps"):
                                url.a_50p().download()

                        if url.a_70()==None:
                            st.button(label="70kbps not available", disabled=True)
                        else:
                            if st.button(label="70kbps"):
                                url.a_70().download()

                        if url.a_128()==None:
                            st.button(label="128kbps not available", disabled=True)
                        else:
                            if st.button(label="120kbps"):
                                url.a_128().download()                        
                    with pic:
                        st.image(url.thumb_nail())
                        st.write(url.title())

                except:
                    st.warning("Enter a valid URL")
                
                
        st.success("Done")


def callback():
    st.session_state.state = True



if __name__ == '__main__':
    main()