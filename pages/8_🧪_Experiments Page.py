import streamlit as st
import time
from CustomComponents import Gallery

def configure():
    # This code reloads saved variables values from session state
    for k in st.session_state.keys():
        st.session_state[k] = st.session_state[k]

    st.set_page_config(
        layout="wide",
        page_icon="🔐",
        page_title="Login",
        initial_sidebar_state="auto"
    )

def main():
    gallery = Gallery
    with st.columns([1, 2, 1])[1]:
        with st.expander("Gallery"):
            gallery.Gallery()

if __name__ == '__main__':
    configure()
    main()
