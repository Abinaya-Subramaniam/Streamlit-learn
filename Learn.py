import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Streamlit Learning")
st.write("The basics of Streamlit, a Python library for creating interactive web apps.")
st.markdown("---")

st.header("1. Displaying Text and Markdown")
st.write("Streamlit makes it easy to display text in different formats. Below are some examples:")

st.text("This is plain text using `st.text`.")

st.markdown("""
### Markdown Examples:
- **Bold Text**
- *Italic Text*
- ~~Strikethrough~~
- `Code Snippet`
- [Link to Streamlit](https://streamlit.io)
""")

st.subheader("Python Code Block Example:")
st.code("""
def greet(name):
    return f"Hello, {name}!"
print(greet('Streamlit'))
""", language="python")

st.markdown("---")

st.header("2. Displaying Data")
st.write("Streamlit supports displaying tables and data easily.")

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'Score': [88, 92, 85]
}

df = pd.DataFrame(data)

st.write("Here's a sample DataFrame:")
st.dataframe(df)

st.write("Here's the same data in a static table:")
st.table(df)

st.subheader("Bar Chart Example:")
st.bar_chart(df[['Score']])

st.markdown("---")

st.header("3. Interactive Widgets")
st.write("Streamlit provides a variety of widgets to make your app interactive.")

# input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! 👋")

age = st.slider("Select your age:", min_value=0, max_value=100, value=25)
st.write(f"Your age is: {age}")

hobby = st.radio("What's your favorite hobby?", options=['Reading', 'Sports', 'Music'])
st.write(f"Your favorite hobby is: {hobby}")

language = st.selectbox("What's your favorite programming language?", options=['Python', 'JavaScript', 'C++', 'Java'])
st.write(f"You chose: {language}")

st.subheader("Upload a CSV File:")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(uploaded_df)

st.markdown("---")

st.header("4. Visualizing Data")
st.write("Streamlit supports several charting libraries like Matplotlib, Altair, and Plotly.")

st.subheader("Line Chart Example:")
chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

st.subheader("Matplotlib Plot Example:")
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y, label='Sine Wave')
ax.set_title("Sine Wave")
ax.legend()
st.pyplot(fig)

st.markdown("---")

st.header("5. Custom Layouts")
st.write("You can create columns, sidebars, and expandable sections for a better app layout.")

col1, col2 = st.columns(2)
with col1:
    st.write("This is Column 1.")
    st.image("pic.png", caption="Matrix1")
with col2:
    st.write("This is Column 2.")
    st.image("pic1.png", caption="Formula")

st.sidebar.title("Sidebar Example")
st.sidebar.write("This is a sidebar for extra content.")
sidebar_choice = st.sidebar.selectbox("Choose a sidebar option:", ["Option 1", "Option 2", "Option 3"])
st.sidebar.write(f"You chose: {sidebar_choice}")

with st.expander("Click to Expand"):
    st.write("This content is hidden until you expand it.")

st.markdown("---")

st.header("6. LaTeX for Math")
st.write("Streamlit supports rendering mathematical expressions using LaTeX.")
st.latex(r"""
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
""")

st.markdown("---")


st.markdown("""
### Thank You! 🤩
""")
