import streamlit as st

st.write("Hello, *World!* :sunglasses:")
st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.markdown("*Streamlit* is **really** ***cool***.")
st.metric(label="Temperature", value="70 °F")
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
  
