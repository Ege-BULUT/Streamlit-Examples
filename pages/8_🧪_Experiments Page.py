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

def title(centered=False):
    title_text = "Experiments Page"
    if centered:
        with st.columns(3)[1]:
            st.title(title_text)
    else:
        st.title(title_text)

def st_gallery(with_expander=True, centered=True):
    gallery = Gallery
    if centered:
        with st.columns([1, 2, 1])[1]:
            if with_expander:
                with st.expander("Gallery"):
                    gallery.Gallery()
            else:
                gallery.Gallery()
    else:
        if with_expander:
            with st.expander("Gallery"):
                gallery.Gallery()
        else:
            gallery.Gallery()

def st_interactive_chart(with_expander=True, centered=False):
    if centered:
        with st.columns([1, 2, 1])[1]:
            if with_expander:
                with st.expander("Interactive Chart"):
                    interactive_chart()
            else:
                interactive_chart()
    else:
        if with_expander:
            with st.expander("Interactive Chart"):
                interactive_chart()
        else:
            interactive_chart()


def interactive_chart():
    separator = st.text_input(max_chars=1, placeholder="Seperator", label=" ", value=",",
                              help=":blue[Seperator]  \nSeparates each one of x and y values.  \n"
                                   ":gray[default seperator: ',']")

    x_raw_input = st.text_input(placeholder="X Values",
                                help=":green[X Values]  \nEnter your x values by separating   \n"
                                     "each individual X value with :blue[seperator]",
                                label=" ")

    allowed_columns = 10
    if x_raw_input != "":
        if st.checkbox("Show X Values:"):
            columns = st.columns(allowed_columns)
            for count, x in enumerate(x_raw_input.split(separator)):
                if count % allowed_columns == 0:
                    columns = st.columns(allowed_columns)
                with columns[count % allowed_columns]:
                    if x != "":
                        try:
                            st.write(float(x))
                        except Exception as _:
                            st.write(str(x))

    y_raw_input = st.text_input(placeholder="Y Values",
                                help=":green[Y Values]  \nEnter your y values by separating  \n"
                                     "each individual Y value with :blue[seperator]",
                                label=" ")

    columns = st.columns(allowed_columns)
    if y_raw_input != "":
        if st.checkbox("Show Y Values:"):
            columns = st.columns(allowed_columns)
            for count, y in enumerate(y_raw_input.split(separator)):
                if count % allowed_columns == 0:
                    columns = st.columns(allowed_columns)
                with columns[count % allowed_columns]:
                    if y != "":
                        try:
                            st.write(float(y))
                        except Exception as _:
                            st.write(str(y))


def main():
    st_gallery(with_expander=True, centered=True)
    st_interactive_chart(with_expander=True, centered=True)

if __name__ == '__main__':
    configure()
    title(centered=True)
    main()
