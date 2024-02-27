import time
import streamlit as st
from CustomComponents import Gallery
import matplotlib.pyplot as pyplot
import plotly.express as plotly


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

    chart_placeholder = st.empty()

    separator = st.text_input(max_chars=1, placeholder="Seperator", label=" ", value=",",
                              help=":blue[Seperator]  \nSeparates each one of x and y values.  \n"
                                   ":gray[default seperator: ',']")

    x_raw_input = st.text_input(placeholder="X Values",
                                help=":green[X Values]  \nEnter your x values by separating   \n"
                                     "each individual X value with :blue[seperator]",
                                label=" ")

    if "values" not in st.session_state.keys():
        st.session_state["values"] = {
            "x": [],
            "y": []
        }
    allowed_columns = 10
    x_values_arr = []
    if x_raw_input != "":
        for count, x in enumerate(x_raw_input.split(separator)):
            if x != "":
                try:
                    x_values_arr.append(float(x))
                except Exception as _:
                    x_values_arr.append(str(x))
        st.session_state["values"]["x"] = x_values_arr if len(x_values_arr) > 0 else st.session_state["values"]["x"]


        show_x = st.checkbox("Show X Values:")
        if show_x:
            mode = st.toggle("Vertical", value=False)
            if mode:
                st.write(st.session_state["values"]["x"])
            else:
                columns = st.columns(allowed_columns)
                for count, x in enumerate(x_values_arr):
                    if count % allowed_columns == 0:
                        columns = st.columns(allowed_columns)
                    if x != "":
                        with columns[count % allowed_columns]:
                            try:
                                st.write(float(x))
                            except Exception as _:
                                st.write(str(x))

    y_raw_input = st.text_input(placeholder="Y Values",
                                help=":green[Y Values]  \nEnter your y values by separating  \n"
                                     "each individual Y value with :blue[seperator]",
                                label=" ")

    y_values_arr = []
    if y_raw_input != "":
        for count, y in enumerate(y_raw_input.split(separator)):
            if y != "":
                try:
                    y_values_arr.append(float(y))
                except Exception as _:
                    y_values_arr.append(str(y))
        st.session_state["values"]["y"] = y_values_arr if len(y_values_arr) > 0 else st.session_state["values"]["y"]


        show_y = st.checkbox("Show Y Values:")
        if show_y:
            mode = st.toggle("Vertical", value=False)
            if mode:
                st.write(st.session_state["values"]["y"])
            else:
                columns = st.columns(allowed_columns)
                for count, y in enumerate(y_values_arr):
                    if count % allowed_columns == 0:
                        columns = st.columns(allowed_columns)
                    if y != "":
                        with columns[count % allowed_columns]:
                            try:
                                st.write(float(y))
                            except Exception as _:
                                st.write(str(y))

    if "isPlotly" not in st.session_state:
        st.session_state["isPlotly"] = False
    if st.session_state["values"]["x"] != [] and st.session_state["values"]["y"] != []:
        c1, c2, c3 = st.columns([8,5,40])
        with c1:
            if not st.session_state["isPlotly"]:
                st.write(":blue[pyplot]")
            else:
                st.write(":gray[pyplot]")
        with c2:
            isPlotly = st.toggle("pyplot | plotly", label_visibility="collapsed", key="isPlotly")
        with c3:
            if st.session_state["isPlotly"]:
                st.write(":blue[plotly]")
            else:
                st.write(":gray[plotly]")

        chart_type = st.selectbox("Chart Type", options=["line", "bar", "scatter", "pie chart"])
        if isPlotly:
            st.session_state["plot_type"] = "pyplot" # previous value
            chart_placeholder.plotly_chart(get_chart(st.session_state["values"]["x"], st.session_state["values"]["y"],
                                            "plotly", chart_type=chart_type), use_container_width=True)
        if not isPlotly:
            st.session_state["plot_type"] = "plotly" # previous value
            chart_placeholder.pyplot(get_chart(st.session_state["values"]["x"], st.session_state["values"]["y"],
                                            "pyplot", chart_type=chart_type), use_container_width=True)


def get_chart(x, y, plt_type, chart_type):
    plot = ""
    if plt_type == "pyplot":
        fig, ax = pyplot.subplots()
        if chart_type == "line":
            ax.plot(x, y, marker="o")
        elif chart_type == "bar":
            ax.bar(x, y)
        elif chart_type == "scatter":
            ax.scatter(x, y)
        elif chart_type == "pie chart":
            if len(x) != len(y):
                st.error("! The length of x and y is not matched !")
                ax.pie(x,)
            else:
                ax.pie(x, labels= y)
        plot = fig

    elif plt_type == "plotly":
        if chart_type == "line":
            plot = plotly.line([x, y], markers=True, x=x, y=y)
        elif chart_type == "bar":
            plot = plotly.bar([x, y], x=x, y=y)
        elif chart_type == "scatter":
            plot = plotly.scatter([x, y], x=x, y=y)
        elif chart_type == "pie chart":
            if len(x) != len(y):
                st.error("! The length of x and y is not matched.")
                plot = plotly.pie(x)
            else:
                plot = plotly.pie([x, y], values=x, names=y, hole=0.2)
                plot.update_traces(textposition='inside', textinfo='percent+label')

    return plot

def main():
    st_gallery(with_expander=True, centered=True)
    st_interactive_chart(with_expander=True, centered=True)

if __name__ == '__main__':
    configure()
    title(centered=True)
    main()
