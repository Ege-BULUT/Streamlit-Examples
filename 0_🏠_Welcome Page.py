import streamlit as st

# This code reloads saved variables values from session state
for k in st.session_state.keys():
    st.session_state[k] = st.session_state[k]

if __name__ == '__main__':
    text = "Welcome"
    if "user" in st.session_state.keys():
        text += " " + st.session_state["user"]["name"]
    st.write(text)
