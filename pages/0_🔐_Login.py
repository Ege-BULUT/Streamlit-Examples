import time
import json
import streamlit as st

users_path = "DB/users.json"


def isUserExists(user, path="DB/users.json"):
    global users_path
    users_path = path if path != users_path else users_path
    users = json.load(open(users_path))
    for key, _user in users.items():
        if _user["name"] == user["name"] and _user["password"] == user["password"]:
            return True
    return False

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

def signup():
    global users_path
    users = json.load(open(users_path))

    arr = [3, 1, 3, 3]
    _, c1, c2, _ = st.columns(arr)
    with c1:
        st.write("Nickname")
    with c2:
        Nickname = st.text_input(key="potential_nickname", label=" ", label_visibility="collapsed")
    _, c1, c2, _ = st.columns(arr)
    with c1:
        st.write("Username")
    with c2:
        Username = st.text_input(key="potential_username", label=" ", label_visibility="collapsed")
    _, c1, c2, _ = st.columns(arr)
    with c1:
        st.write("Password")
    with c2:
        Password = st.text_input(key="potential_pw", label=" ", label_visibility="collapsed", type="password")
    _, c1, c2, _ = st.columns(arr)
    with c1:
        st.write("Repeat Password")
    with c2:
        st.text_input(key="potential_pw2", label=" ", label_visibility="collapsed", type="password")
    _, c1, c2, _ = st.columns(arr)
    with c1:
        st.write("Email")
    with c2:
        Email = st.text_input(key="potential_email", label=" ", label_visibility="collapsed")


    user_info = {
        "name"  : Username,
        "password"  : Password,
        "email"     : Email,
    }
    with c2:
        if st.button("Create account"):
            # VALIDATE USER to check if its OK for saving it into DB
            # if so
            users.update({Nickname: user_info})
            json.dump(users, fp=open(users_path, "w"), indent=4)

def login():
    with st.columns(3)[1]:
        username = st.text_input("Username")

        pw_previous = "" if "user" not in st.session_state.keys() else st.session_state["user"]["password"]
        pw = st.text_input("Password", type="password")

        if (st.button("log in") and pw != pw_previous) or pw != pw_previous:
            user = {
                "name": username,
                "password": pw
            }
            if isUserExists(user):
                st.session_state.update({"user": user})
                st.session_state.pop("login_page_state")
                st.rerun()
            else:
                warn = st.error("Username or Password is invalid!", icon="❗")
                time.sleep(1)
                warn.empty()

def already_logged_in():
    user = st.session_state["user"]
    c1, c2, _ = st.columns([3, 6, 40])
    with c1:
        if st.button("log out"):
            st.session_state.pop("user")
            st.rerun()
    with c2:
        if st.button("Home Page"):
            st.switch_page("1_🏠_HomePage.py")


def main():
    if "user" in st.session_state.keys():
        st.write("Welcome", st.session_state["user"]["name"])
    if "user" not in st.session_state.keys() or st.session_state["user"]["name"] == "":
        c1, c2, _ = st.columns([1, 2, 15])
        with c1:
            btn_login = st.empty()
        with c2 :
            btn_signup = st.empty()
        if btn_login.button("Login"):
            st.session_state["login_page_state"] = "login"
        if btn_signup.button("Create Account"):
            st.session_state["login_page_state"] = "signup"

        if "login_page_state" in st.session_state.keys():
            if st.session_state["login_page_state"] == "login":
                # btn_login.empty()
                # btn_signup.empty()
                login()
            elif st.session_state["login_page_state"] == "signup":
                # btn_login.empty()
                # btn_signup.empty()
                signup()


    else:
        already_logged_in()



if __name__ == '__main__':
    configure()
    main()
