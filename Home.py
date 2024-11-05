import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2, vertical_alignment="top")

with col1:
    st.image("static/photo.jpg", use_column_width="auto")

with col2:
    st.title("Jonathan L")
    content = """
    
      python developer \n
      passionated to work in real world projects
      
     
    """
    st.info(content)
    st.link_button("GitHub", "https://github.com/dashboard")

st.divider()

content2 = """ 
Below you can find some of the apps I have build in Python, Feel free to contact me! 
"""
st.markdown(":blue[**Below you can find some of the apps I have build in Python, Feel free to contact me!**]")


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:5].iterrows():
        st.header(row["title"], divider=True)
        st.write(row["description"])
        # st.image("static/img/" + row["image"])
        st.button("Source Code", row['url'])


with col4:
    for index, row in df[5:].iterrows():
        st.header(row["title"], divider=True)
        st.write(row["description"])
        # st.image("static/img/" + row["image"])
        st.button("Source Code", row['url'])