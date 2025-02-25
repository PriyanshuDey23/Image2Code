import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from Image2Code.helper import process_image


# Streamlit app setup
st.set_page_config(layout="wide", page_title="Design to Website App", page_icon="✨")

st.title("✨ Design to Website Generator")
st.markdown("Convert your design images into a functional website effortlessly.")

# Initialize session state variables
if "html" not in st.session_state:
    st.session_state["html"] = ""
if "image" not in st.session_state:
    st.session_state["image"] = ""

# Layout for file upload and result display
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.subheader("📤 Upload Your Design Image")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        with st.spinner("Processing your image..."):
            image_path = uploaded_file.name
            image = Image.open(uploaded_file)
            image.save(image_path)

            # Display the uploaded image
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

            # Save the image path in session state
            st.session_state.image = image_path
        st.button("🚀 Generate HTML", on_click=process_image)

with col2:
    st.subheader("🖥️ Generated HTML Preview")
    if st.session_state.html:
        with st.expander("📜 View Source Code"):
            st.code(st.session_state.html, language="html")
        st.markdown("---")
        with st.container():
            styled_html = f"""
            <div style="
                border: 1px solid #ddd; 
                padding: 10px; 
                border-radius: 10px; 
                background-color: #f9f9f9;">
                {st.session_state.html}
            </div>
            """
            components.html(styled_html, height=600, scrolling=True)
    else:
        st.info("🔄 The generated HTML will appear here once the process is complete.")

