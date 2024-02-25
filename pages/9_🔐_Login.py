import streamlit as st

# This code reloads saved variables values from session state
for k in st.session_state.keys():
    st.session_state[k] = st.session_state[k]

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
            # else display a warning





def already_logged_in():
    user = st.session_state["user"]
    st.write("You are already logged in as")
    st.write(user["name"])
    if st.button("log out"):
        st.session_state.pop("user")


if __name__ == '__main__':
    if "user" in st.session_state.keys() and st.session_state["user"]["name"] != "":
        already_logged_in()
    else:
        login()
