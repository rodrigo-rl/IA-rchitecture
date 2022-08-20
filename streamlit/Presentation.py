import streamlit as st
import base64

st.title("IA rchitecture")
#st.header('Learn about the style of your favourite buildings!')
st.header("")
st.subheader('Discover the architectural style of your favourite building just with a photo')
st.subheader('Thanks of a IA model you can learn more about architecture*')
st.header("")
col1, col2 =st.columns(2)

#operation description
col1.subheader("1 - Upload the picture")
col1.text("")
col1.subheader("2 - Confirm")
col1.text("")
col1.subheader("3 - Enjoy the info!")

#image of the process
col2.image("Explanation.jpg")

st.text("")
st.text("")
st.text("We are working on add more styles, currently there are the following styles:")
col1, col2, col3, col4,col5 =st.columns(5)

col1.text("1- Postmodern style\n2- Novelty architecture\n3- International style\n4- Deconstructivsm\n5- Chicago School")

st.sidebar.image("Architecture.gif")