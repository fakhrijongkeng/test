import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components

# 1. Prepare your data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [25, 30, 35, 40, 45, 50, 55],
    'City': ['New York', 'London', 'Paris', 'New York', 'London', 'Paris', 'New York'],
    'Salary': [50000, 60000, 75000, 80000, 90000, 100000, 110000],
    'Years_Experience': [2, 5, 8, 10, 12, 15, 18]
}
df = pd.DataFrame(data)

# --- Streamlit Application ---

# Set Streamlit page configuration (optional but recommended for wide layout)
st.set_page_config(
    page_title="PyGWalker in Streamlit",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Interactive Data Exploration with PyGWalker")

st.write("---") # Add a separator for better visual organization

st.header("Original Data")
st.dataframe(df) # Display the DataFrame in Streamlit

st.write("---")

st.header("PyGWalker Interactive Explorer")

# Option 1: Use pyg.walk and embed the HTML (simpler for basic use)
# This will generate the HTML for the PyGWalker UI and embed it directly.
# The `return_html=True` is crucial here.
pyg_html = pyg.walk(df, return_html=True)
components.html(pyg_html, height=1000, scrolling=True)

# Option 2: Use the PyGWalker Streamlit API (more advanced, allows state saving)
# This is recommended for more complex applications or when you want to save
# the chart configuration.
# from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
#
# # Establish communication between pygwalker and streamlit
# init_streamlit_comm()
#
# # You should cache the renderer instance to prevent memory issues with large datasets
# @st.cache_resource
# def get_pyg_renderer() -> "StreamlitRenderer":
#     # Set debug=False in production to prevent users from modifying config files
#     return StreamlitRenderer(df, spec="./gw_config.json", debug=False, spec_io_mode="rw")
#
# renderer = get_pyg_renderer()
#
# # Render your data exploration interface
# renderer.render_explore()

st.write("---")
st.info("You can drag and drop fields in the PyGWalker interface above to create visualizations!")