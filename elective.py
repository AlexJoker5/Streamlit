import streamlit as st

esub = st.selectbox("Elective : ", ['Music', 'Korean', 'Japanese'])

st.write("Your elective subject is : ", esub)

hobbies = st.multiselect("Hobbies : ", ['Painting', 'Music', 'Sports'])

st.write("You selected : ", len(hobbies) , 'hobbies')

if(st.button("Click me.. Click me")):
    st.text("Hello! Welcome to Streamlit")

name = st.text_input("Enter your name ", "Type Here ...")

if(st.button('Submit')):
    result = name.title()
    st.write("Hello ",result)