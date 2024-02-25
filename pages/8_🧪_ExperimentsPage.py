import streamlit as st
import time

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

def main():
    with st.columns([1, 2, 1])[1]:
        if "images" in st.session_state.keys():
            images = st.session_state.images
        else:
            images = get_images()
            if images is not None and len(images) > 0:
                st.session_state["images"] = images

        if len(images) > 0:
            gallery(images)

        if st.button("Empty Image List"):
            st.session_state.pop("images")
            st.success("Images erased successfully!")
            time.sleep(1)
            st.rerun()


def get_images():
    images = st.file_uploader("Upload images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    return images

def gallery(images):
    value = (st.session_state["image_index"] if st.session_state["image_index"] <= len(images) else 1) if "image_index" in st.session_state.keys() else 1
    if "image_index" in st.session_state.keys():
        st.session_state["image_index"] = st.session_state["image_index"] if st.session_state["image_index"] <= len(images) else 1
    index = st.number_input(key="image_index", label=" ", label_visibility="collapsed",
                            min_value=1, max_value=len(images), value=value, step=1)

    image = images[index-1]

    st.image(image, use_column_width=True)

if __name__ == '__main__':
    configure()
    main()
