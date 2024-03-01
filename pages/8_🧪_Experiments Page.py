import io
import time
import plotly.io as pio
import streamlit as st
from CustomComponents import Gallery
import matplotlib.pyplot as pyplot
import plotly.graph_objects as go


pio.templates.default = "plotly"

for k in st.session_state.keys():
    st.session_state[k] = st.session_state[k]
if "latest_index" not in st.session_state.keys():
    st.session_state["latest_index"] = []

def st_vertical_space(amount):
    for i in range(amount):
        st.write(" ")

def configure():
    # This code reloads saved variable values from the session state

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



# # # GENERIC INPUTS # # #

def st_input(item, show_label):
    default_types = {
        bool: "toggle",
        str: "text_input",
        int: "number_input",
        float: "number_input"
    }

    item["label"] = item["label"] if "label" in item.keys() else item["value"].__class__.__name__ + " input"

    print("debug : ", item)
    _label = item["label"]
    _value = item["value"]
    _help  = item["help"] if "help" in item.keys() else None
    _type  = item["type"] if "type" in item.keys() else default_types
    _key   = item["key"]
    output_value = ""

    if "hidden" in item.keys() and item["hidden"]:
        print("hidden true", item["label"])
        return {item["key"]: item["value"]}

    else:
        print("hidden false", item["label"])
        if show_label:
            _label_visibility = "visible"
        else:
            _label_visibility = "collapsed"

        if "multi_select" in item.keys() and item["multi_select"]:
            _options = item["options"]
            if _type == "select_slider":
                output_value = st.select_slider(label=_label, options=_options, value=_value, label_visibility=_label_visibility, help=_help )
            elif _type == "selectbox":
                output_value = st.selectbox(label=_label, options=_options, index=_options.index(_value), label_visibility=_label_visibility, help=_help )
            elif _type == "multiselect":
                output_value = st.multiselect(label=_label, options=_options, label_visibility=_label_visibility, help=_help, default=_value )

        if _type == "number_input":
            output_value = st.number_input(label=_label, help=_help, value=_value, label_visibility=_label_visibility)
        if _type == "slider":
            output_value = st.slider(label=_label, help=_help, value=_value, label_visibility=_label_visibility)
        elif _type == "text_input":
            output_value = st.text_input(label=_label, help=_help, value=_value, label_visibility=_label_visibility)
        elif _type == "password":
            output_value = st.text_input(label=_label, help=_help, value=_value, type="password", label_visibility=_label_visibility)
        elif _type == "toggle":
            output_value = st.toggle(label=_label, help=_help, value=_value, label_visibility=_label_visibility)
        elif _type == "checkbox":
            output_value = st.toggle(label=_label, help=_help, value=_value, label_visibility=_label_visibility)

        return {_key: output_value}


def prepare_pack(items):
    latest_index = len(st.session_state["latest_index"])

    pack = {"value": items,
             "label": items.__class__.__name__ + " input",
             "help": "Default value is : :blue[" + str(items) + "]",
             "key": str(items) + "_" + items.__class__.__name__,
            }

    return pack

def generate_inputs(items, input_positions=None, show_labels=True, label_position="top"):
    default_types = {
        bool: "toggle",
        str: "text_input",
        int: "number_input",
        float: "number_input"
    }
    if input_positions is None:
        try:
            input_positions = [st.container(), st.expander("Advanced")]
        except Exception as e:
            normal_inputs = st.container()
            advanced_inputs = st.container()
            input_positions = [normal_inputs, advanced_inputs]
    elif type(input_positions) is not list:
        input_positions = [input_positions, input_positions]

    latest_index = len(st.session_state["latest_index"])


    label_visibility = "visible" if (show_labels and label_position == "top") else "collapsed"

    # IF input iterable is not an iterable (single value)
    if type(items) in [str, int, bool, float]:
        items = prepare_pack(items)
        items.update({"label_visibility": label_visibility})
        values = generate_inputs(items, input_positions, show_labels, label_position)
        return values
    elif type(items) in [list, set, tuple]:
        values = dict()
        for item in items:
            value_2 = generate_inputs(item, input_positions=input_positions, show_labels=show_labels, label_position=label_position)
            values.update(value_2)
        return values
    elif type(items) is dict:
        if "value" not in items.keys():
            dict_arr = []
            for key1, value1 in items.items():
                temp_dict = {
                    "key": key1,
                    "label": key1.replace("_", " ").capitalize(),
                    "value": value1,
                    "type": default_types[type(value1)]
                }
                dict_arr.append(temp_dict)
            return generate_inputs(dict_arr, input_positions=input_positions, show_labels=show_labels, label_position=label_position)
        else:
            if "type" not in items.keys():
                items.update({"type": default_types[type(items["value"])]})
            if "key" not in items.keys():
                items.update({"key": str(items["value"]) + "_" + items.__class__.__name__})
            items.update({"label_visibility": label_visibility})
            if "advanced" in items.keys() and items["advanced"]:
                with input_positions[1]:
                    values = st_input(items, show_label=show_labels )
            elif "hidden" in items.keys() and items["hidden"]:
                return {items["key"]: items["value"]}
            else:
                with input_positions[0]:
                    values = st_input(items, show_label=show_labels )
            #st.session_state["latest_index"].append(values)
            return values




def example_generic_inputs():
    with st.expander("Generic Inputs"):
        # Single value example

        c1, c2, c3 = st.columns([3, 3, 3])
        with c1:
            st.subheader("Single value example")
            st.write("generate_inputs(':blue[abc]')")
            returned_value = generate_inputs("abc")
            c11, c12 = st.columns([2,4])
            with c11:
                st.write("returned value is")
            with c12:
                st.write(":orange["+str(returned_value)+"]")
        with c2:
            st.subheader("Single value detailed example")
            st.write("generate_inputs(  \n{'value': :blue[5],  'type':':blue[slider]',  'label':':blue[number slider]'})")
            returned_value = generate_inputs({'value': 5, 'type': 'slider', 'label': 'number slider'})
            c11, c12 = st.columns([2,4])
            with c11:
                st.write("returned value is")
            with c12:
                st.write(":orange["+str(returned_value)+"]")
        with c3:
            st.subheader("Multi value example")
            st.write("generate_inputs([1, 'abc', True])")
            returned_value = generate_inputs([1, 'xyz', True])
            c11, c12 = st.columns([2,4])
            with c11:
                st.write("returned value is")
            with c12:
                st.write(":orange["+str(returned_value)+"]")

        c1, c2, c3 = st.columns([1, 3, 1])
        with c2:
            st.subheader("Multi value detailed example")
            st.text("generate_inputs("
                     "  \n  ["
                     "  \n    {'value': 10, 'type': 'slider'},"
                     "  \n    {'value': 100},"
                     "  \n    {'value': 'ege bulut'},"
                     "  \n    {'value': 'ege.the.engineer', type='password'},"
                     "  \n    {'value': 'ege', 'multi_select':True, 'type': 'multiselect',"
                     "  \n     'options':['ege','bulut','the', 'engineer']},"
                     "  \n    {'value': 'ege', 'multi_select':True, 'type': 'select_slider',"
                     "  \n     'options':['ege','bulut','the', 'engineer']},"
                     "  \n    {'value': 'ege', 'multi_select':True, 'type': 'selectbox',"
                     "  \n     'options':['ege','bulut','the', 'engineer']},"
                     "  \n  ]"
                     "  \n)")

            returned_value = generate_inputs([{'value': 10, 'type': 'slider'}, {'value': 100}, {'value': 'ege bulut'}, {'value': 'ege.the.engineer', "type": 'password'},
                                {'value': 'ege', 'multi_select': True, 'type': 'multiselect',   'options': ['ege', 'bulut', 'the', 'engineer']},
                                {'value': 'ege', 'multi_select': True, 'type': 'select_slider', 'options': ['ege', 'bulut', 'the', 'engineer']},
                                {'value': 'ege', 'multi_select': True, 'type': 'selectbox',     'options': ['ege', 'bulut', 'the', 'engineer']},]
                        )
            c11, c12 = st.columns([2, 4])
            with c11:
                st.write("returned value is")
            with c12:
                st.write(":orange[" + str(returned_value) + "]")


def main():
    st_gallery(with_expander=True, centered=True)
    st_interactive_chart(with_expander=True, centered=True)
    example_generic_inputs()

if __name__ == '__main__':
    configure()
    title(centered=True)
    main()
