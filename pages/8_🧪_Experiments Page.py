import io
import time
import plotly.io as pio
import streamlit as st
from CustomComponents import Gallery
import matplotlib.pyplot as pyplot
import plotly.graph_objects as go


pio.templates.default = "plotly"

def st_vertical_space(amount):
    for i in range(amount):
        st.write(" ")




def configure():
    # This code reloads saved variable values from the session state
    for k in st.session_state.keys():
        st.session_state[k] = st.session_state[k]

    st.set_page_config(
        layout="wide",
        page_icon="🧪",
        page_title="Experiments Page",
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


def interactive_chart(downloadable=True):
    if "isPlotly" not in st.session_state:
        st.session_state["isPlotly"] = False

    chart_placeholder = st.empty()

    if downloadable:
        buffer = io.BytesIO()
        _, c1, c2, _ = st.columns([4, 5, 5, 4])
        with c1:
            st_vertical_space(2)
            download_btn = st.empty()
        with c2:
            if st.session_state["isPlotly"]:
                download_file_type = st.selectbox(help=":blue[File Type]", options=["html"],
                                                  index=0, label=" ")

            else:
                download_file_type = st.selectbox(help=":blue[File Type]", options=["svg", "png", "jpg", "pdf", "webp"],
                                                  index=0, label=" ")
            mime_types = {
                "png": "image/png",
                "jpg": "image/jpeg",
                "svg": "image/svg+xml",
                "pdf": "application/pdf",
                "webp": "image/webp",
                "html": "text/html",
            }

    _, c1, c2, c3, _ = st.columns([3, 1, 1, 1, 3])
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


        show_x = st.checkbox("Show X Values:", key="show_x")
        if show_x:
            mode = st.toggle("Vertical", value=False, key="vertical_x")
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


        show_y = st.checkbox("Show Y Values:", key="show_y")
        if show_y:
            mode = st.toggle("Vertical", value=False, key="vertical_y")
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


        chart_type = st.selectbox("Chart Type", options=["line", "bar", "scatter", "pie chart"])
        if isPlotly:
            plot = get_chart(st.session_state["values"]["x"], st.session_state["values"]["y"],
                             plt_type="plotly", chart_type=chart_type)
            chart_placeholder.plotly_chart(plot, use_container_width=True)
            if downloadable:
                plot.write_image(file=buffer, format="svg")

        if not isPlotly:
            plot = get_chart(st.session_state["values"]["x"], st.session_state["values"]["y"],
                                            plt_type="pyplot", chart_type=chart_type)
            chart_placeholder.pyplot(plot, use_container_width=True)
            if downloadable:
                plot.savefig(buffer, format=download_file_type)

    if downloadable:
        download_btn.download_button(
            label="Download Plot",
            data=buffer,
            file_name="Plot_"+str(time.time())+"."+download_file_type,
            mime=mime_types[download_file_type],
        )


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
        plot = go.Figure()
        if chart_type == "line":
            plot.add_trace(go.Scatter(x=x, y=y))
        elif chart_type == "bar":
            plot.add_trace(go.Bar([x, y], x=x, y=y))
        elif chart_type == "scatter":
            plot.add_trace(go.Scatter([x, y], x=x, y=y))
        elif chart_type == "pie chart":
            if len(x) != len(y):
                st.error("! The length of x and y is not matched.")
                plot.add_trace(go.Pie(x))
            else:
                plot.add_trace(go.Pie(values=x, labels=y, hole=0.2))
                plot.update_traces(textposition='inside', textinfo='percent+label')

    return plot

def main():
    st_gallery(with_expander=True, centered=True)
    st_interactive_chart(with_expander=True, centered=True)

if __name__ == '__main__':
    configure()
    title(centered=True)
    main()
