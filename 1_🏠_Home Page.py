import streamlit as st


def configure():
    # This code reloads saved variables values from session state
    for k in st.session_state.keys():
        st.session_state[k] = st.session_state[k]

    st.set_page_config(
        layout="wide",
        page_icon="🏠",
        page_title="Home",
        initial_sidebar_state="auto"
    )


def main():
    text = "Welcome "
    text += st.session_state["user"]["name"] if "user" in st.session_state.keys() else "Guest"
    st.write(text)


if __name__ == '__main__':
    configure()
    main()
