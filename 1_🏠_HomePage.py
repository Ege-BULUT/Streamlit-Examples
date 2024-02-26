import streamlit as st

pages = {
    "Home Page" : {"path":"1_🏠_HomePage.py", "icon": "🏠"},
    "Login Page" : {"path":"pages/0_🔐_Login.py", "icon": "🔐"},
    "Experiments Page" : {"path":"pages/8_🧪_Experiments Page.py", "icon": "🧪"},
}

def st_vertical_space(amount):
    for i in range(amount):
        st.write(" ")


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
    st.write(":blue[" + text+"]")
    st_vertical_space(3)
    st.write("where would you want to go?")
    for page_label, page_info in pages.items():
        st.page_link(page=page_info["path"], label=page_label, icon=page_info["icon"])

if __name__ == '__main__':
    configure()
    main()
