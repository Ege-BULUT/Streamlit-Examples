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
    # This code reloads saved variable values from the session state
    for k in st.session_state.keys():
        st.session_state[k] = st.session_state[k]

    st.set_page_config(
        layout="wide",
        page_icon="🏠",
        page_title="Home",
        initial_sidebar_state="auto"
    )

def welcome():
    text = "Welcome "
    text += st.session_state["user"]["nickname"] if "user" in st.session_state.keys() else "Guest"
    st.write(":blue[" + text+"]")

def navigation():
    st.write("where would you want to go?")
    for page_label, page_info in pages.items():
        st.page_link(page=page_info["path"], label=page_label, icon=page_info["icon"])

def body():
    with st.expander("About", expanded=True):
        description = """
        This Project provides open source boilerplate Streamlit App Templates for different use-cases. 
        """
        st.text(description)
        columns = st.columns([1, 6])
        with columns[0]:
            st.write(":green[Main Branch]  \n" +
                     ":green[LEVEL 0 Template]  \n" +
                     ":green[LEVEL 1 Template]  \n" +
                     ":green[Development Branch]")
        with columns[1]:
            st.write(": [Github repository](https://github.com/Ege-BULUT/Streamlit-Examples)  \n" +
                     ": [STARTER](https://github.com/Ege-BULUT/Streamlit-Examples/tree/BOILERPLATE-0-STARTER)  \n" +
                     ": [BASIC](https://github.com/Ege-BULUT/Streamlit-Examples/tree/BOILERPLATE-1-BASIC)  \n" +
                     ": [DEV](https://github.com/Ege-BULUT/Streamlit-Examples/tree/DEV)")
def main():
    st.title("Home Page")
    welcome()
    st_vertical_space(3)
    navigation()
    st_vertical_space(3)
    body()

if __name__ == '__main__':
    configure()
    main()
