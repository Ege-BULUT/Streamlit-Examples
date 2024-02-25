import streamlit as st

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

def login():
    with st.columns(3)[1]:
        username = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.button("log in"):
            # Connect to a db or local list of unames, upws and check
            # if user exists, login
            user = {
                "name": username,
                "password" : pw
            }
            st.session_state.update({"user": user})
            st.rerun()
            # else display a warning

def already_logged_in():
    user = st.session_state["user"]
    with st.columns([2, 4])[0]:
        msg = st.success("Logged in successfully as " + user["name"] + " !")
    c1, _, c2, _ = st.columns([2, 1, 2, 7])
    with c1:
        if st.button("log out"):
            st.session_state.pop("user")
            st.rerun()
    with c2:
        if st.button("Home Page"):
            st.switch_page("0_🏠_WelcomePage.py")


def main():
    if "user" in st.session_state.keys() and st.session_state["user"]["name"] != "":
        already_logged_in()
    else:
        login()


if __name__ == '__main__':
    configure()
    main()
