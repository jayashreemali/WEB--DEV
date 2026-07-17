import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="My First Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Title and description
st.title("🚀 Welcome to Streamlit.my first app")
st.write("Build interactive web apps using only Python!")

# Sidebar
st.sidebar.header("Settings")

name = st.sidebar.text_input(
    "Enter your name",
    "Intern"
)

age = st.sidebar.slider(
    "Select your age",
    10,
    50,
    20
)

# Display user information
st.subheader("User Information")

st.write(f"Hello, **{name}**!")
st.write(f"Your age is **{age}** years.")

# Sample data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.subheader("Sample Data")
st.dataframe(data)

# Line chart
st.subheader("Line Chart")
st.line_chart(data)

# Button
if st.button("Click Me"):
    st.success("Button clicked successfully!")

# Checkbox
if st.checkbox("Show Code"):
    st.code("""
import streamlit as st

st.title("Hello Streamlit")
st.write("My first app")
""")